#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_MPU6050.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

Adafruit_MPU6050 mpu;

RF24 radio(7, 8); // CE, CSN
const byte address[6] = "00001";

void setup() {
  Wire.begin();
  mpu.begin();
  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
}

void loop() {
  sensors_event_t event;
  mpu.getEvent(&event);

  float x_accel = event.acceleration.x;
  radio.write(&x_accel, sizeof(x_accel));
  delay(200);
}
