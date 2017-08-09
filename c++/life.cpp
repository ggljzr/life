#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

#define DISPLAY_NAME "Game of Life"
#define KEY_ESC 27
#define KEY_SPACE 32
#define KEY_ENTER 10
#define KEY_ALT 233
#define KEY_S 115

int main(int argc, char ** argv)
{
    int w = 200;
    int h = 200;

    cv::Mat display = cv::Mat::zeros(w, h, CV_8UC1);
    cv::namedWindow(DISPLAY_NAME, 1);

    cv::imshow(DISPLAY_NAME, display);

    bool exit = false;
    while(!exit)
    {
        int key = (cv::waitKey() & 0xEFFFFF);
        switch(key)
        {
            case KEY_ESC:
                exit = true;
                break;
        }
    }

    return 0;
}