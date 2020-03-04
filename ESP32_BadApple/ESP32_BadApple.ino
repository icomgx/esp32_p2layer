#include <WiFi.h>
#include <U8g2lib.h>
#include <U8x8lib.h>

char* ssid     = "iCOMgx"; //填写你的wifi名字
char* password = "sshiki123"; //填写你的wifi密码

uint8_t apple[1024] = {};   //定义缓冲区 128 * 64 / 8 = 1024
const uint8_t result_msg[1] = {0x00}; //定义返回信息

WiFiClient client; //初始化一个客户端对象

U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE); //构建u8g2



void setup() {
  WiFi.begin(ssid, password); //连接wifi
  u8g2.begin(); //初始化u8g2
  delay(1000); //等待1秒
  if (WiFi.status() == WL_CONNECTED) //判断如果wifi连接成功
  {
    const int httpPort = 715; //设置上位机端口
    client.connect("192.168.31.177", httpPort); //连接到上位机，ip改成你的局域网ip
    client.write(result_msg, 1); //发送返回信息
  }
}

void loop() {
  while (client.available()) {   //如果TCP的缓冲区有数据
    client.read(apple, 1024);    //从缓冲区读取 1024长度的数据写入 apple[]
    drawApple(apple);            //调用drawApple方法
    client.write(result_msg, 1); //发送返回信息
  }
}


void drawApple(uint8_t a2pple[1024])
{
  u8g2.clearBuffer();             //清除缓冲区 清屏
  u8g2.drawXBMP(0, 0, 128, 64, a2pple); //在（坐标x, 坐标y, 图像宽度, 图像高度, 图像数组）绘制图像
  u8g2.sendBuffer();              // 发送到缓冲区 显示
}
