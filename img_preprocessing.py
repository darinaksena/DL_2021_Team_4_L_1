import cv2
import os

PATH = 'flowers10'
DATASET_PATH = 'dataset'
TRAIN_PATH = DATASET_PATH + '/train'
VALID_PATH = DATASET_PATH + '/valid'
TEST_PATH = DATASET_PATH + '/test'
IMG_SIZE = 224

def process(src_path, res_path):
    img = cv2.imread(src_path, cv2.IMREAD_COLOR)

    crop_factor = min(img.shape[0], img.shape[1]) / IMG_SIZE

    if img.shape[1] > img.shape[0]:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    resized = cv2.resize(img, (int(img.shape[0] / crop_factor), int(img.shape[1] / crop_factor)))

    delta = (max(resized.shape[0], resized.shape[1]) - IMG_SIZE) // 2
    start = delta
    end = delta + IMG_SIZE
    if resized.shape[1] > resized.shape[0]:
        cropped = resized[:, start:end]
    else:
        cropped = resized[start:end, :]

    cv2.imwrite(res_path, cropped)


def mkdir(path):
    try:
        os.mkdir(path)
    except BaseException:
        pass

if __name__ == '__main__':

    mkdir(DATASET_PATH)
    mkdir(TRAIN_PATH)
    mkdir(VALID_PATH)
    mkdir(TEST_PATH)
    for clazz in range(1, 11):
        class_path = PATH + '/{}'.format(clazz)
        files = os.listdir(class_path)

        mkdir(TRAIN_PATH + '/{}'.format(clazz) + '/')
        mkdir(VALID_PATH + '/{}'.format(clazz) + '/')
        mkdir(TEST_PATH + '/{}'.format(clazz) + '/')

        for i in range(0, 15):
            path = class_path + '/' + files[i]
            new_path = TRAIN_PATH + '/{}'.format(clazz) + '/' + files[i]
            process(path, new_path)

        for i in range(15, 20):
            path = class_path + '/' + files[i]
            new_path = VALID_PATH + '/{}'.format(clazz) + '/' + files[i]
            process(path, new_path)

        for i in range(20, 30):
            path = class_path + '/' + files[i]
            new_path = TEST_PATH + '/{}'.format(clazz) + '/' + files[i]
            process(path, new_path)

