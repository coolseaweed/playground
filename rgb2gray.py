import cv2
import argparse
import os


def get_args():
    parser = argparse.ArgumentParser()


    parser.add_argument('--input_path', type=str,
                        required=True,
                        help="""input img path
                        """)
    parser.add_argument('--output_path', type=str,
                        default='./result',
                        help="""input img path
                        """)
    args = parser.parse_args()

    return args


def main():
    FLAGS = get_args()
    
    os.makedirs(FLAGS.output_path,exist_ok=True)
    img_path = FLAGS.input_path
    filename=os.path.basename(img_path)
    
    rgb_img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
    
    cv2.imwrite('./result/'+filename, gray_img)
    print('done!')


if __name__ == '__main__':
    main()
