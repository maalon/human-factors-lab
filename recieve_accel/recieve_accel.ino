#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN
const byte address[6] = "00001";

float prev_time = 0;
float prev_speed = 0;

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.startListening();
}

void loop() {
  if (radio.available()) {
    float x_accel;
    radio.read(&x_accel, sizeof(x_accel));
    float current_time = millis();
    float dt = current_time - prev_time;
    float speed = prev_speed + (x_accel * dt);
    Serial.println(speed);
    prev_time = current_time;
    prev_speed = speed;
    delay(200);
  }
}
