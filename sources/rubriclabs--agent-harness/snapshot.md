A harness is the software that translates a model into a system that can affect its environment.

For example, [Pi](https://pi.dev/) is a harness that lets the model use your terminal to read and edit files on your computer.

Functionally, a harness makes a model agentic, meaning it can take action.

Put simply:

Agent = Model + Harness

A few of the harnesses we'll discuss in this post include [Claude Code](https://rubriclabs.com/blog/how-does-claude-code-actually-work), Codex, Cursor, OpenClaw, Hermes and Pi. They generally share the same underlying functional areas.

## [Looping](https://rubriclabs.com/blog/what-is-an-agent-harness#loop)

At a minimum, a harness collects LLM calls in a loop (even ChatGPT has a harness). A common looping architecture is ReAct (Reason + Act), where a user sends a message and the agent thinks, searches, writes code, and responds when it's done.

The agent loop
Modern harnesses go much further: they let agents work for a long time, learn from experience, and delegate work.

## [Context](https://rubriclabs.com/blog/what-is-an-agent-harness#context)

Every time the agent loops, the harness passes context to the inference endpoint. Context is all the information the model can see to decide what to do next. A common pattern is to include:

- a fixed system prompt (which describes the agent's role)

- some current information (today's date, preferences, available tools)

- the past messages (user messages, tool calls, tool outputs and agent messages) in chronological order

LLMs have finite context windows (a maximum amount of information they can process at a time) and an agent that loops enough will often fill up this window. So we have to choose which parts of the total context to keep.

A context window filling up
Harnesses largely use two strategies that address different parts of the problem: compaction and memory.

### [Compaction](https://rubriclabs.com/blog/what-is-an-agent-harness#compaction)

Harnesses largely deal with context limits within a single run using a compaction strategy, where they ask an LLM to summarize historic information, and then remove it from the window.

Compaction within a single run
Good compaction can be [the difference](https://x.com/OpenAI/status/2082616640144048433) between stunted and outstanding performance.

When a session ends, its compacted context is generally discarded.

What if we want an agent to learn over time and across sessions?

### [Memory](https://rubriclabs.com/blog/what-is-an-agent-harness#memory)

Humans actually have [a few](https://www.psychologytoday.com/ca/basics/memory/types-of-memory) types of memory, such as procedural (how to), episodic (what happened), and tacit (intuition).

Most harnesses today collapse memory into procedural vs. everything else.

A common way to store procedural memory is in skills. Skills are folders that include markdown text describing a workflow, and optionally scripts that aid that workflow. Encoding your IP into high quality, opinionated skills is a powerful way to scale your leverage with agents. Harnesses determine how to create and use skills.

Tacit knowledge is the unwritten heuristics and intuition gained from experience. Modern harnesses generally bucket it into MEMORY.md (and, to a lesser extent, USER.md).

Memory carried across sessions
Memory is one of the areas of AI engineering that feels largely unsolved. It's unclear whether it will be solved through scaling LLM capabilities or necessitates a new architecture. Many AI engineers believe that "continual learning" is necessary for true AGI, where the model's weights actually change over time as it interacts with the world. This would likely imply that procedural and episodic memory, world knowledge and intuition become subsumed into the black box.

## [Orchestration](https://rubriclabs.com/blog/what-is-an-agent-harness#orchestration)

We'll look at two mechanisms an agent uses to orchestrate its work: planning and dispatch.

### [Planning](https://rubriclabs.com/blog/what-is-an-agent-harness#planning)

As coding agents begin to run for longer, and deploy more intelligence through [dispatch](https://rubriclabs.com/blog/what-is-an-agent-harness#dispatch), they are owning larger and more complex problems end to end, and the developer is less in the loop to steer the agent. The value of high quality planning increases as agents implement the plans more autonomously. Harnesses like [Claude Code](https://rubriclabs.com/blog/how-does-claude-code-actually-work) and Codex ship with a native planning mode, where the agent must first create a detailed Plan.md file with feedback from the user before executing. These harnesses then place a reference to the plan and the todo list into a top level state (system prompt) so that the agent doesn't forget what it's working on across long runs.

### [Dispatch](https://rubriclabs.com/blog/what-is-an-agent-harness#dispatch)

For complex tasks, modern harnesses enable the primary agent to delegate work to one or many sub-agents. This is powerful because it enables the agent to elastically scale to meet the complexity of the task, but it also introduces complexity because you have to coordinate across fragmented state. Without a coherent orchestration strategy, agents can overwrite each other's work, get caught in loops, or lose track of the core task.

Orchestration is one of the newer components of agentic engineering as we transition from single agent runtimes into agent fleets and agent swarms. A common strategy for coding agents is to have the main agent come up with a plan and a todo list for a large build, and then dispatch one agent per todo list item, and then one agent to review each item.

A primary agent dispatching three sub-agents
NewsletterThe Grid
What we’re learning about building with AI. Two short emails a month.

## [Tools](https://rubriclabs.com/blog/what-is-an-agent-harness#tools)

### [Execution](https://rubriclabs.com/blog/what-is-an-agent-harness#execution)

Agents interact with the outside world using tool calls. A common pattern is to define tools through an input schema and output schema. The LLM outputs JSON text that is compatible with the input schema, then the harness interprets that and executes actual code (such as executing an API call), awaits the response, and returns data to the model with the result of the action.

The harness's solution for transforming LLM tool calls into actual function executions on computers carries strong implications for how the system thinks about authorization and autonomy. For example, do you sign in to your email account in a browser and give the agent tooling to control the browser? Or do you expose tools to read, draft and send emails, then execute those actions through your email provider's API with OAuth?

### [Interfaces](https://rubriclabs.com/blog/what-is-an-agent-harness#mcp)

MCP (Model Context Protocol) servers have emerged as a standard interface for scaling tools.

Historically, developers have had to write bespoke integration code for every tool they want to use. In the email example, the harness would have to host code that translates the LLM's email.send payload into an authenticated API call to the email provider, and every other harness would have to do the same.

With MCP, the community or email providers themselves can build this tooling once, and the harnesses just need to adopt MCP broadly.

MCP is by no means necessary: CLIs or simply good documentation offer similar benefits.

## [Verification](https://rubriclabs.com/blog/what-is-an-agent-harness#verification)

As the plans we give agents get harder and touch more complex surface area, it becomes paramount to evaluate whether solutions actually work. Today, most harnesses leave this largely up to the model and tooling, or encode frameworks in the system prompt. In the code world, AI systems are encouraged to write unit tests, and use tools like Computer Use and Browser Use to conduct smoke tests.

Unit tests can end up being low-signal, as the agent often writes the test with full context of how their code works, and adds an arbitrary check mark on something that may not actually work.

Smoke tests can catch the kinds of issues that usually surface through use. In a smoke test, an agent walks through the final product, sanding down any rough edges it encounters.

AI Labs are increasingly post-training their models using reinforcement learning environments where the model is set up with a harness, so it's possible that verification becomes an emergent model level instinct and doesn't need to be an opinion of the harness.

A reviewer checking a sub-agent’s work

## [Permissions](https://rubriclabs.com/blog/what-is-an-agent-harness#permissions)

When an agent wants to do an action such as executing code on a computer, the harness needs to decide whether that action can be executed immediately, or if the action needs to be reviewed for safety. Harnesses like Codex historically required the user to review every new action the agent wanted to take on the computer, and allow that action once or in perpetuity. Users could bypass this setting with "YOLO mode", which approves every request automatically.

Newer iterations often include an autonomous AI review where all actions are passed into an LLM for review and a request is only surfaced to the user if the LLM deems it "risky". Permission granularity evolves as users build trust in the previous generation of systems.

## [What's next for harnesses?](https://rubriclabs.com/blog/what-is-an-agent-harness#future)

Harnesses represent a major new lever to scaling AI output, alongside model size, data, and compute. They can unlock [18x cost savings](https://x.com/OpenAI/status/2082616640144048433) and [superhuman scores](https://www.primeintellect.ai/blog/prime-agent) on complex puzzles, and foundation models are increasingly being [trained](https://x.com/liquidai/status/2084640701669613906) with harnesses in mind.

Seeing such dramatic improvements on hard problems, we can only imagine what's possible in real-world settings.
