import re
import sys
import json
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

csv_path = sys.argv[1]#'./sentences.csv'
output_path = sys.argv[2]#'./output.jsonl'


# reading files
df = pd.read_csv(csv_path)
print(f"Loaded file with shape of {df.shape}")

# preprocess then used NLTK for word to convert to POS_TAGs 
def get_word_tokenize_with_pos_tag(sentence):
    sentence = pre_process(sentence)
    words = word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)
    word_list = []
    pos_tags_list = []
    for sent, tag in pos_tags:
        word_list.append(sent)
        pos_tags_list.append(tag)
    return (word_list, pos_tags_list)


# Extract featues with tag is IN
def extract_features(sentence_number, sentences):
    tokens, pos_tags = get_word_tokenize_with_pos_tag(sentences)
    prepositions = [i for i, token_tag in enumerate(zip(tokens, pos_tags)) if (token_tag[1] == 'IN') and 
                    (token_tag[0].lower() in ['on', 'for', 'of', 'to', 'at', 'in', 'with', 'by'])]
    result = []
    
    for prep_position in prepositions:
        prep_id = f"{sentence_number}_{prep_position}"
        prep = tokens[prep_position]
        
        features = [
            ' '.join(tokens[max(0, prep_position-1):prep_position]),
            ' '.join(tokens[prep_position:prep_position+2]),
            ' '.join(tokens[max(0, prep_position-1):prep_position+2]),
            ' '.join(tokens[max(0, prep_position-2):prep_position]),
            ' '.join(tokens[prep_position:prep_position+3]),
            ' '.join(tokens[max(0, prep_position-2):prep_position+3]),
            ' '.join(pos_tags[max(0, prep_position-1):prep_position]),
            ' '.join(pos_tags[prep_position:prep_position+2]),
            ' '.join(pos_tags[max(0, prep_position-1):prep_position+2]),
            ' '.join(pos_tags[max(0, prep_position-2):prep_position]),
            ' '.join(pos_tags[prep_position:prep_position+3]),
            ' '.join(pos_tags[max(0, prep_position-2):prep_position+3]),
        ]
        result.append({
            "id": prep_id,
            "prep": prep,
            "features": features
        })
    return result



# replace end sentences and new sentences
def pre_process(sent):
    sent = sent.replace('.', '').replace(',', '')
    return sent


# data frame columns which having sentences flattern to list for process.
def process_sentences(df):
    sentences = df['Sentence'].tolist()
    output = []
    for i, sentence in enumerate(sentences, start=1):
        output.extend(extract_features(i, sentence))
    return output


def write_output_json(output_path, output_data):
    with open(output_path, 'w') as f:
        for line in output_data:
            f.write(json.dumps(line) + '\n')
        f.close()
    print(f"Look Output file to {output_path}")

def main():
    output_data = process_sentences(df)

    # Write output to a jsonlines file
    write_output_json(output_path, output_data)


if __name__ == "__main__":
    main()




