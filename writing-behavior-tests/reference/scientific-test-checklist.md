# Scientific Test Checklist

- Is the test asserting a real contract?
- Can it fail for the right reason?
- Is the random seed or stochastic distribution recorded?
- Are tolerances justified by numerical method and precision?
- Are hardware, compiler, backend, or simulator versions recorded when relevant?
- Does the test survive an implementation-preserving refactor?
- Is the test readable without knowing the chat history?
