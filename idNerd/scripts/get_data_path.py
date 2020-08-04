import os, glob, random

if __name__ == "__main__":
    import argparse
    # Parse comment line arguments
    parser = argparse.ArgumentParser(
        description='get the data paths and output the train.txt and test.txt')
    parser.add_argument("--datapath", type=str, 
                        metavar="path to ", 
                        default="/mnt/mlserver/datasets/chips",
                        help="darknet data path")
    parser.add_argument("--train_val_ratio", type=float, 
                        metavar="path to ", 
                        default=0.8,
                        help="split ratio of trian val")
    parser.add_argument("--type", type=str, 
                        metavar="image file type", 
                        default="jpg",
                        help="image type used in dataset")            
    parser.add_argument("--output", type=str, 
                        metavar="Logging file", 
                        default="/mnt/mlserver/models/darknet",
                        help="where to store the files")
    args = parser.parse_args()

    images = glob.glob1(args.datapath, '*.'+args.type)
    print(images[:5])
    random.shuffle(images)
    print(images[:5])

    n_train = int(len(images)*args.train_val_ratio)

    trainPath = os.path.join(args.output, "train.txt")
    mode = "a"
    if not os.path.exists(trainPath):
        mode = "w+"
    trainFile = open(trainPath, mode)
    for i, img in enumerate(images[:n_train]):
        trainFile.write(f'{os.path.join(args.datapath, img)}\n')
    trainFile.close()

    if args.train_val_ratio < 1.0:
        valPath = os.path.join(args.output, "val.txt")
        mode = "a"
        if not os.path.exists(valPath):
            mode = "w+"
        valFile = open(valPath, mode)
        for i, img in enumerate(images[n_train:]):
            valFile.write(f'{os.path.join(args.datapath, img)}\n')
        valFile.close()