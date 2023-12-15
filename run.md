## Runing Script (Python code)


Certainly! Below is a `run.md` file that you can include with your solution. This file provides instructions on how to run your Python script:


## Running the Feature Extraction Script

To use the provided Python script for feature extraction, follow the instructions below:

1. **Clone the Repository:**

```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository

```

Replace `yourusername` and `yourrepository` with your GitHub username and repository name.

2. **avigate to the Repository:**


```bash
   cd path_to_gitdir

```
Replace `path_to_gitdir` with the actual path to the cloned repository.


3. **Run the Feature Extraction Script:**
Use the following commands to run the Python script:

```bash
python Code_Logic.py csv_path output_json_path

```

Replace csv_path with the path to your CSV file containing sentences and part-of-speech tags, and output_json_path with the desired path for the output JSONlines file.
For example:


```bash
python Code_Logic.py sentences.csv output.json

```

Check the Output:
After running the script, you will find the output in the specified JSONlines file (`output.json`). Each line in the file corresponds to a preposition in the input sentences, along with its features.

4. **Check the Output:**

```json

{"id": "1_5", "prep": "in", "features": ["entered in", "in to", "entered in to", "once entered in", "in to the", "once entered in to the", "VBN IN", "IN TO", "VBN IN TO", "RB VBN IN", "IN TO DT", "RB VBN IN TO DT"]}
```

Ensure that the output format matches the requirements.
