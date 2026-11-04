"""Synthetic negative controls for intent annotation integrity."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('intent_check',Path(__file__).resolve().parents[1]/'check-intent-classification.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class IntentIntegrity(unittest.TestCase):
    def fixture(self):
        window=dict(id='W',alias='SYNTHETIC',messages=[dict(item_id='u1',role='userMessage',text='Draft only.'),dict(item_id='a1',role='agentMessage',text='Sent it.'),dict(item_id='u2',role='userMessage',text='Do not send.')])
        r=dict(alias='SYNTHETIC',selection_id='W',rubric_sha256='rubric',window_sha256=hashlib.sha256(json.dumps(window,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),phase_purpose=['execute'],human_contribution=['reaffirm_requirement'],agent_response=['conflicts_with_established_state'],clarity={x:'explicit' for x in ['objective','deliverable','audience','constraints','success_criterion','action_authority']},clarity_rationale='Synthetic',interpretation_limits='Synthetic; no real send',human_review_status='unreviewed',training_eligible=False,allowed_uses=['private_analysis'],dataset_split='development',evidence_refs=[dict(item_id='u1')],evaluated_action_refs=['a1'],decision=dict(establishment_refs=['u1']),decision_time_cutoff='u1',information_state='captured_at_cutoff',violation_status='supported',violation_requirement_ref='u1',violation_action_ref='a1',violation_rationale='Draft-only preceded claimed sending.')
        return r,window
    def test_valid_order(self):
        r,w=self.fixture();self.assertTrue(m.check(r,w,'rubric'))
    def test_later_requirement_cannot_prove_earlier_violation(self):
        r,w=self.fixture();r['violation_requirement_ref']='u2'
        with self.assertRaises(ValueError):m.check(r,w,'rubric')
    def test_unknown_context_cannot_support_violation(self):
        r,w=self.fixture();r['information_state']='unknown'
        with self.assertRaises(ValueError):m.check(r,w,'rubric')
    def test_model_review_cannot_become_human_approval(self):
        r,w=self.fixture();r['human_review_status']='confirmed'
        with self.assertRaises(ValueError):m.check(r,w,'rubric')
    def test_window_and_rubric_drift_rejected(self):
        r,w=self.fixture();w['messages'][0]['text']='Changed'
        with self.assertRaises(ValueError):m.check(r,w,'rubric')
        r,w=self.fixture()
        with self.assertRaises(ValueError):m.check(r,w,'different rubric')
    def test_unknown_locator_rejected(self):
        r,w=self.fixture();r['evaluated_action_refs']=['absent']
        with self.assertRaises(ValueError):m.check(r,w,'rubric')
    def test_repair_cannot_replace_the_prior_action(self):
        r,w=self.fixture();r['evaluation_focus']='prior_action';r['prior_action_refs']=['a1'];r['evaluated_action_refs']=['u2']
        with self.assertRaises(ValueError):m.check(r,w,'rubric')

if __name__=='__main__':unittest.main()
