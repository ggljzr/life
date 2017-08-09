#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <time.h>
#include <stdlib.h>
#include <unistd.h>

#define DISPLAY_NAME "Game of Life"
#define KEY_ESC 27
#define KEY_SPACE 32
#define KEY_ENTER 10
#define KEY_ALT 233
#define KEY_S 115

int getNeigboursSum(const cv::Mat * mat, int x, int y)
{
    int rows = mat->rows;
    int channels = mat->channels();
    int cols = mat->cols * channels;

    int sum = 0;
    for(int i = y - 1; i <= y + 1;i ++)
    {
        if(i < 0 || i >= rows)
            continue;

        const uchar* row = mat->ptr<uchar>(i);

        for(int j = x - channels; j <= x + channels; j += channels)
        {
            if(j < 0 || j >= cols || (j == x && i == y))
                continue;
            //printf("[%d][%d] = %d\n", i, j, row[j]);
            //sum += row[j] / 255;
            int inc = 0;
            for(int c = 0; c < channels; c++)
            {
                inc = row[j + c] || inc;
            }
            sum += inc;
        }
    }

    return sum;
}

int initGame(cv::Mat * mat)
{
    int rows = mat->rows;
    int cols = mat->cols * mat->channels();
    int channels = mat->channels();

    for(int i = 0; i < rows; i++)
    {
        uchar * row = mat->ptr<uchar>(i);
        for(int j = 0; j < cols; j += channels)
        {
            if((rand() % 3) == 0)
            {
                int color = rand() % channels;
                row[j + color] = 255;
            }
            else
            {
                for(int c = 0; c < channels; c++)
                    row[j + c] = 0;
            }
        }
    }
}

void step(cv::Mat * mat)
{
    int rows = mat->rows;
    int cols = mat->cols * mat->channels();
    int channels = mat->channels();
    cv::Mat newMat = cv::Mat::zeros(mat->rows, mat->cols, mat->type());

    for(int i = 0; i < rows; i++)
    {
        uchar * row = mat->ptr<uchar>(i);
        uchar * newRow = newMat.ptr<uchar>(i);
        for(int j = 0; j < cols; j += channels)
        {
            int neighbours = getNeigboursSum(mat, j, i);
            if(neighbours < 2 || neighbours > 3)
            {
                for(int c = 0; c < channels; c++)
                    newRow[j + c] = 0;
            }
            else if(neighbours == 3)
            {
                for(int c = 0; c < channels; c++)
                    newRow[j + c] = 0;
                int color = rand() % channels;
                newRow[j + color] = 255;
            }
            else
            {
                for(int c = 0; c < channels; c++)
                    newRow[j + c] = row[j + c];
            }
        }
    }

    newMat.copyTo(*mat);
}

int main(int argc, char ** argv)
{
    int w = 800;
    int h = 800;

    srand(time(NULL));

    cv::Mat display = cv::Mat::zeros(h, w, CV_8UC3);
    initGame(&display);
    cv::namedWindow(DISPLAY_NAME, 1);

    //std::cout << display << std::endl;
    //std::cout << getNeigboursSum(&display, 3,1) << std::endl;

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
            case KEY_SPACE:
                step(&display);
                cv::imshow(DISPLAY_NAME, display);
                break;
        }
    }

    return 0;
}