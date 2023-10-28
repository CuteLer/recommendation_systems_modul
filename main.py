import pandas as pd
import json

def read_file():
    df_metrics_de = pd.DataFrame(columns=['AccountID', 'Data'])

    with open('data/metrics_ru.txt') as file:
        while True:
            string = (file.readline().replace('\n', '').replace('\t', ''))
            if string:
                temp = pd.DataFrame([[string[:6], string[6:]]], columns=['AccountID', 'Data'])
                # df_metrics_de = df_metrics_de.append(temp, ignore_index=True)
                df_metrics_de = pd.concat([df_metrics_de, temp], ignore_index=True)

            else:
                break

    df_metrics_de['Data'] = df_metrics_de['Data'].apply(json.loads)
    df_metrics_de = pd.concat([df_metrics_de.drop(['Data'], axis=1), df_metrics_de['Data'].apply(pd.Series)], axis=1)
    df_metrics_de.to_csv('metrics_ru.csv')

if __name__ == '__main__':
    ...
