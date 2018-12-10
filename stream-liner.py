import cv2
import sys

def laugh(fl_name):

    # Gray Scaleで画像を読み込み
    gray_img = cv2.imread(fl_name, 0)

    # Cannyアルゴリズムでエッジ検出
    canny_edges = cv2.Canny(gray_img, 100, 200)

    f = lambda x:x >> 8 - 1

    while(1):

        # エッジ検出の結果をループ
        for horizon_elm in canny_edges:

            laugh_lst = []

            for elm in horizon_elm:
                laugh_lst.append(str(f(elm)))

            print("".join(laugh_lst))

if __name__ == '__main__':

    argvs = sys.argv

    img_file = argvs[1]

    laugh(img_file)
