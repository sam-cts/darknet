import os, glob, random

if __name__ == "__main__":
    import argparse
    # Parse comment line arguments
    parser = argparse.ArgumentParser(
        description='get the data paths and output the train.txt and test.txt')
    parser.add_argument("--datapath", type=str, 
                        metavar="path to ", 
                        default="/datasets/Chips/darknet_data",
                        help="darknet paths")
    args = parser.parse_args()
    
    images = glob.glob1(args.datapath, '*.png')
    print(f'first 10 images before shuffle: \n{images[:10]}')
    random.shuffle(images)
    print(f'first 10 images after  shuffle: \n{images[:10]}')

    n_data = len(images)
    n_train = int(n_data*0.6)
    n_valid = int((n_data - n_train)/2)
    n_test = n_data - n_train - n_valid

    def write_darknet_data_file(filename, imgNames):
        filepath = os.path.join(args.datapath, filename)
        txt_file = open(filepath, 'a')
        for imgName in imgNames:
            imgPath = os.path.join(args.datapath,imgName)
            txt_file.write(f'{imgPath}\n')
        txt_file.close()

    train = images[:n_train]
    valid = images[n_train:n_train+n_valid]
    test = images[n_train+n_valid:]

    write_darknet_data_file('train.txt', train)
    write_darknet_data_file('valid.txt', valid)
    write_darknet_data_file('test.txt', test)
