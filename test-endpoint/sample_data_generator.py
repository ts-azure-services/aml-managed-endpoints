import argparse
import json
import pandas as pd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--number_of_records', required=True, help='The number of records to generate.')
    args = parser.parse_args()

    ## Get existing data
    base_data = pd.read_csv('./data/credit-card-data-original.csv')
    base_data = base_data.drop('default payment next month', axis=1)

    # Compute number of generations
    record_count = int(args.number_of_records)
    batches, remainder = None, None
    if record_count > base_data.shape[0]:
        batches, remainder = int( record_count / base_data.shape[0]), int( record_count % base_data.shape[0] )
        print(f"Number of records: {record_count}, number of batches: {batches}, remaining records: {remainder}")
        df = pd.DataFrame()
        for round in range(0,batches):
            df = pd.concat([df, base_data])
            #df.append(base_data)#.sample(record_count))
        # Get remainder added
        df = pd.concat([df,base_data.sample(remainder)])
    else:
        df = base_data.sample(n=record_count)
        print(f"Number of records: {record_count}, number of batches: {batches}, remaining records: {remainder}")

    # Reset index on final dataframe
    df = df.reset_index(drop=False)
    df = df.drop(['index', 'ID'], axis=1)
    print(f"Final dataframe length: {len(df)}")

    # Convert to json
    if record_count > 100000:
        df.to_csv(f'./test-endpoint/{args.number_of_records}_inference_data.csv', encoding='utf-8', index=False)
    else:
        existing_values = df.to_json(orient='split')
        new_dict = {'input_data': existing_values}
        filename = f'./test-endpoint/{args.number_of_records}_inference_data.json'
        with open(filename, 'w') as f:
            json.dump(new_dict, f)
