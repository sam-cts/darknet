import os, glob, random

def write_darknet_data_file(filename, imgNames, outpath):
    filepath = os.path.join(outpath, filename)
    txt_file = open(filepath, 'a')
    for imgName in imgNames:
        imgPath = os.path.join(outpath,imgName)
        txt_file.write(f'{imgPath}\n')
    txt_file.close()

def split_dataset(images, outpath):
    n_data = len(images)
    n_train = int(n_data*0.6)
    n_valid = int((n_data - n_train)/2)
    n_test = n_data - n_train - n_valid

    train = images[:n_train]
    valid = images[n_train:n_train+n_valid]
    test = images[n_train+n_valid:]

    write_darknet_data_file('train.txt', train, outpath)
    write_darknet_data_file('valid.txt', valid, outpath)
    write_darknet_data_file('test.txt', test, outpath)


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
    random.shuffle(crowdimgs)
    split_dataset(crowdimgs, args.outpath)
    chipstackimgs = glob.glob1(args.chipstack, '*.png')
    random.shuffle(chipstackimgs, args.outpath)



