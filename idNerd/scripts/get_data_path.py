import os, glob

if __name__ == "__main__":
    import argparse
    # Parse comment line arguments
    parser = argparse.ArgumentParser(
        description='get the data paths and output the train.txt and test.txt')
    parser.add_argument("--datapath", type=str, 
                        metavar="path to ", 
                        default="/datasets/Chips/darknet_data",
                        help="darknet paths")
    parser.add_argument("--train_val_ratio", type=float, 
                    metavar="path to ", 
                    default=0.8,
                    help="split ratio of trian val")                 
    parser.add_argument("--output", type=str, 
                        metavar="Logging file", 
                        default="/datasets/Chips/darknet_data")
    args = parser.parse_args()

    images = glob.glob1(args.datapath, '*.png')

    n_train = int(len(images)*args.train_val_ratio)

    trainFile = open(os.path.join(args.output, "train.txt"), "a")
    valFile = open(os.path.join(args.output, "val.txt"), "a")

    for i, img in enumerate(images):
        if i < n_train:
            trainFile.write(f'{os.path.join(args.output, img)}\n')
        else:
            valFile.write(f'{os.path.join(args.output, img)}\n')
    trainFile.close()
    valFile.close()