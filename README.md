## Test-Case-Generation-using-LLM

# Overview:
Test-Case-Generation-using-LLM" is an innovative approach to enhancing regression testing by integrating Large Language Models (LLMs), such as Gemini, with Control Flow Graph (CFG) analysis. This project aims to automate the generation of regression test cases, ensuring comprehensive coverage and efficiency in software testing.

# Features:
* <mark>Automated Test Case Generation</mark>: Utilizes LLMs to generate exhaustive and diverse test cases, achieving 96.4% precision and 85.1% recall in regression test selection.
* <mark>Control Flow Graph Analysis</mark>: Employs CFGs to assess the quality of test cases and identify critical paths influenced by code changes.
* <mark>Efficient Test Suite Maintenance</mark>: Implements a dual classification system to categorize test cases as outdated, relevant, or new, optimizing regression testing processes.

# Methodology  

1) <mark>Initial Test Case Generation</mark>: The system uses LLMs to produce a comprehensive set of initial test cases based on the original code version.
2) <mark>Versioning and Prompt Augmentation</mark>: Generates secondary prompts to create new test cases reflecting code modifications, ensuring continued validity.
3) <mark>Control Flow Graph Validation</mark>: Utilizes CFGs to validate and map execution paths, ensuring thorough testing and identification of obsolete test cases.
4) <mark>Refinement and Combination</mark>: Combines relevant test cases from all code versions, forming a robust and efficient regression test suite.

# Experimental Results
* Demonstrated significant improvements in test coverage and bug detection compared to traditional methods.
* Validated through experiments showing high precision in identifying and categorizing test cases.

# Limitations and Future Work
* <mark>Structural Consistency</mark>: Requires identical syntactic structures for effective CFG comparison.
* <mark>Zero-shot Response Errors</mark>: Occasionally, the LLM may not provide accurate zero-shot responses.
* <mark>Scope and Language Limitations</mark>: Initial analysis focused on Python; further research needed for broader applicability.

# References
1) [Effective Test Generation Using Pre-trained Large Language Models and Mutation Testing](https://arxiv.org/abs/2308.16557)
2) [Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting using LLM](https://arxiv.org/abs/2402.00097)
