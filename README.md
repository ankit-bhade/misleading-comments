# Lying Comments

Can a misleading code comment trick AI into the wrong bug fix?

Team project: Ankit Bhade, Arnav Yennam, Kushal Upreti, Seung Wook Jung. Instructor: Dr. Bowen Xu, NC State.

The plan is in `Project Proposal.pdf`.

## Adding a program
1. Read `DATA_STANDARD.md`.
2. Copy `example/count_pairs/` to `programs/<your_function_name>/` and edit it.
3. Check it (this also saves the 4 versions to `versions/`):
   ```
   python3 check.py programs/<your_function_name>
   ```
4. Commit and push, or open a pull request so a teammate can review your comments.

No git? On GitHub, open the `programs` folder, choose **Add file → Upload files**, and drag in your folder.

## Generating the main set (27 programs each)
Open your AI coding tool in the repo and say: "Read GENERATING.md and make my 27 programs. My name is ___."

## Running the model on your programs
We run the model on Google Colab with `colab_run.ipynb`. Steps are in `EXPERIMENT.md`. Results go in `results/`; commit and push them.
