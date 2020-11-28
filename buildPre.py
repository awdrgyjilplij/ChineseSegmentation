from pathlib import Path

dataPath = Path('data')
trainPath = Path(dataPath, 'train.txt')
devPath = Path(dataPath, 'dev.txt')
preDevPath=Path(dataPath, 'preDev.txt')
preTrainPath=Path(dataPath, 'preTrain.txt')

out=[]
# with open(trainPath,encoding='utf-8') as train_f:
#     for line in train_f:
#         line=line.strip().split()
#         out.append(''.join(line))

# with open(preTrainPath,'w',encoding='utf-8') as preTrain_f:
#     for line in out:
#         preTrain_f.write(line+'\n')

# out.clear()
with open(devPath,encoding='utf-8') as dev_f:
    for line in dev_f:
        line=line.strip().split()
        out.append(''.join(line))

with open(preDevPath,'w',encoding='utf-8') as preDev_f:
    for line in out:
        preDev_f.write(line+'\n')