# coding: utf-8

import os
import json
import pandas as pd


def get_input_path(catype, mod):
    input_path = os.path.join('../data/', catype, mod)
    return input_path


def load_json(input_path, json_name='profile.json'):

    file_name = os.path.join(input_path, json_name)

    try:
        f = open(file_name, 'r')
        json_data = json.load(f)
        f.close()

        print(file_name + "is correctly loaded")

        return json_data

    except IOError:
        print("Cannot Open" + file_name)


def json2df(json_data):
    '''
    load sample_type, pathologic, fileid
    '''

    sample_num = len(json_data)

    sample_types = []
    pathology_report_uuids = []
    file_ids = []

    for n in range(sample_num):
        sample_types.append(json_data[n]['cases'][0]['samples'][0]['sample_type'])
        pathology_report_uuids.append(json_data[n]['cases'][0]['samples'][0]['pathology_report_uuid'])
        file_ids.append(json_data[n]['file_id'])

    df = pd.DataFrame(
        {'file_id': file_ids,
         'pathology_report_uuid': pathology_report_uuids,
         'sample_type': sample_types})

    return df


def save_df(catype, mod, df):

    output_dir = '../output/'
    output_name = catype + '.' + mod + '.clinical_data.csv'
    df.to_csv(os.path.join(output_dir, output_name))

    return


if __name__ == "__main__":

    catype = 'TCGA_BRCA'
    mod = 'RNAseq'

    input_path = get_input_path(catype, mod)
    json_data = load_json(input_path)

    df = json2df(json_data)
    save_df(catype, mod, df)
