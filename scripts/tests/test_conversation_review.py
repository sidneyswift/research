"""Regression checks for corpus review integrity; no real conversation data."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS=Path(__file__).resolve().parents[1]
def module(name):
    spec=importlib.util.spec_from_file_location(name,SCRIPTS/(name+'.py'))
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

class ReviewIntegrity(unittest.TestCase):
    def test_recorder_preserves_annotations_and_restrictions(self):
        sys.path.insert(0,str(SCRIPTS))
        recorder=module('record-conversation-reviews')
        note=dict(alias='C0001',episode_observation='Synthetic',interpretation_limits='Synthetic',
                  interventions=[dict(feedback_item_id='m2')],lesson_candidates=['Scoped candidate'],
                  source_reuse_restricted=True,excluded_from_training_and_publication=True,
                  review_kind='full-visible-projection-with-exact-block-dedup',
                  exact_block_dedup=dict(unique_bodies=1,occurrences=2))
        result=recorder.annotation_fields(note)
        for key in ['interventions','lesson_candidates','source_reuse_restricted','excluded_from_training_and_publication','exact_block_dedup']:
            self.assertEqual(result[key],note[key])
        with self.assertRaises(ValueError):recorder.annotation_fields(dict(note,training_eligible=True))
        with self.assertRaises(ValueError):recorder.annotation_fields(dict(note,interventions=4))
        del note['exact_block_dedup']
        with self.assertRaises(ValueError):recorder.annotation_fields(note)

    def test_secret_display_redaction(self):
        redact=module('read-conversation-review').redact
        fixtures=['password is 739268','flxpak_'+'a'*48,'https://local/callback?code=privatecode&state=privatestate','API_KEY=privatekey','password\n```\nprivatepassword\n```','credential 12345678-1234-1234-1234-123456789abc']
        secrets=['739268','a'*48,'privatecode','privatestate','privatekey','privatepassword','12345678-1234-1234-1234-123456789abc']
        for fixture in fixtures:
            result=redact(fixture)
            for secret in secrets:self.assertNotIn(secret,result)

    def merge(self, *, inspected=True, duplicate=False, update=False):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);private=root/'private';run=root/'run';private.mkdir();run.mkdir()
            messages=[dict(item_id='m1',text='User asks a question'),dict(item_id='m2',text='[external_agent_tool_call: AskUserQuestion]\nA real question\n[/external_agent_tool_call]')]
            queue=[dict(alias='C0001',messages=messages,chars=123,source_sha256='synthetic',status='pending')]
            cov=[dict(alias='C0001',source_sha256='synthetic',semantic_review_status='pending')]
            r=dict(alias='C0001',id='REVIEW-C0001',source_ref='sources/codex--conversation-corpus-20261102#C0001',review_kind='full-dialogue-with-tool-inventory',reviewed_message_ids=['m1','m2'],reviewed_dialogue_message_ids=['m1'],inventoried_tool_message_ids=['m2'],inspected_tool_evidence_ids=['m2'] if inspected else [],tool_payload_review_limits='Synthetic tool payload fully read',human_review_status='unreviewed',training_eligible=False,episode_observation='Revised finding',interpretation_limits='Synthetic')
            if duplicate:r['reviewed_message_ids']=['m1','m1','m2']
            (private/'review-queue.json').write_text(json.dumps(queue))
            (run/'coverage.jsonl').write_text(json.dumps(cov[0])+'\n')
            (run/'reviews.jsonl').write_text(json.dumps(dict(r,episode_observation='Old finding'))+'\n' if update else '')
            (run/'reviews-agent-a.jsonl').write_text(json.dumps(r)+'\n')
            result=subprocess.run([sys.executable,str(SCRIPTS/'merge-conversation-review-shards.py'),'--private-corpus',str(private),'--run',str(run)],capture_output=True,text=True)
            rows=(run/'reviews.jsonl').read_text()
            return result.returncode,rows

    def test_valid_typed_review(self):self.assertEqual(self.merge()[0],0)
    def test_question_payload_cannot_be_inventory_only(self):self.assertNotEqual(self.merge(inspected=False)[0],0)
    def test_duplicate_message_coverage_rejected(self):self.assertNotEqual(self.merge(duplicate=True)[0],0)
    def test_later_review_correction_propagates(self):
        status,rows=self.merge(update=True);self.assertEqual(status,0);self.assertIn('Revised finding',rows);self.assertNotIn('Old finding',rows)

    def test_derived_views_preserve_restrictions_and_missing_context(self):
        with tempfile.TemporaryDirectory() as tmp:
            run=Path(tmp)
            review=dict(id='REVIEW-C0001',alias='C0001',source_ref='sources/example#C0001',
                        reviewed_message_ids=['m1','m2'],episode_observation='Synthetic case',
                        interpretation_limits='Not independently verified',source_reuse_restricted=True,
                        excluded_from_training_and_publication=True,
                        interventions=[dict(feedback_item_id='m2',observation='Synthetic feedback')],
                        lesson_candidates=[dict(lesson='Chat-scoped candidate')])
            (run/'reviews.jsonl').write_text(json.dumps(review)+'\n')
            result=module('build-conversation-learning-views').build(run)
            self.assertEqual(result,dict(interventions=1,lessons=1))
            intervention=json.loads((run/'interventions.jsonl').read_text())
            lesson=json.loads((run/'lessons.jsonl').read_text())
            self.assertEqual(intervention['evidence_refs'],[dict(alias='C0001',item_id='m2')])
            self.assertEqual(lesson['evidence_scope'],'chat-level')
            self.assertIsNone(intervention['context_cutoff'])
            self.assertIsNone(intervention['desired_target'])
            self.assertTrue(lesson['excluded_from_training_and_publication'])
            self.assertFalse(lesson['training_eligible'])

    def test_triage_counts_are_not_learning_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            run=Path(tmp)
            (run/'reviews.jsonl').write_text(json.dumps(dict(id='R',alias='C0001',source_ref='sources/example',reviewed_message_ids=['m'],episode_observation='Synthetic',interpretation_limits='Synthetic',observed_interventions=2,lesson_candidates=1))+'\n')
            self.assertEqual(module('build-conversation-learning-views').build(run),dict(interventions=0,lessons=0))

    def test_unknown_annotation_locator_is_not_silently_discarded(self):
        builder=module('build-conversation-learning-views')
        with self.assertRaises(ValueError):
            builder.local_ids(dict(evidence_ids=['item-999']),{'item-1'})

if __name__=='__main__':unittest.main()
