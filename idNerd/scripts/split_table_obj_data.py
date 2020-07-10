import os, glob, random

def write_darknet_data_file(filename, imgPaths, outpath):
    filepath = os.path.join(outpath, filename)
    txt_file = open(filepath, 'a')
    for imgPath in imgPaths:
        # imgPath = os.path.join(outpath,imgName)
        txt_file.write(f'{imgPath}\n')
    txt_file.close()

def split_dataset(images):
    n_data = len(images)
    n_train = int(n_data*0.6)
    n_valid = int((n_data - n_train)/2)
    n_test = n_data - n_train - n_valid

    train = images[:n_train]
    valid = images[n_train:n_train+n_valid]
    test = images[n_train+n_valid:]

    return train, valid, test


if __name__ == "__main__":
    import argparse
    # Parse comment line arguments
    parser = argparse.ArgumentParser(
        description='get the data paths and output the train.txt and test.txt')
    parser.add_argument("--crowd", type=str, 
                        metavar="path to ", 
                        default="/datasets/Chips/darknet_data",
                        help="darknet paths")
    parser.add_argument("--chipstack", type=str, 
                    metavar="path to ", 
                    default="/datasets/Chips/darknet_data",
                    help="darknet paths")
    parser.add_argument("--outpath", type=str, 
                    metavar="path to output", 
                    default="/datasets/Chips/darknet_data",
                    help="darknet paths")
    args = parser.parse_args()
    
    crowdimgs = glob.glob1(args.crowd, '*.jpg')
    crowdimgs = [os.path.join(args.crowd, img) for img in crowdimgs]
    chipstackimgs = glob.glob1(args.chipstack, '*.png')
    chipstackimgs = [os.path.join(args.chipstack, img) for img in chipstackimgs]

    train, valid, test = split_dataset(crowdimgs)
    train_chips, valid_chips, test_chips = split_dataset(chipstackimgs)

    train.extend(train_chips)
    random.shuffle(train) 
    valid.extend(valid_chips)
    random.shuffle(valid)
    test.extend(test_chips)
    random.shuffle(test)

    write_darknet_data_file('train.txt', train, args.outpath)
    write_darknet_data_file('valid.txt', valid, args.outpath)
    write_darknet_data_file('test.txt', test, args.outpath)
