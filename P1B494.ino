#include <AltSoftSerial.h>

#include "I2Cdev.h"
#include "MPU6050.h"

#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif

AltSoftSerial S;

MPU6050 accelgyro;

int16_t ax, ay, az;
int16_t gx, gy, gz;

void setup() {
  Serial.begin(9600);
  //  Serial.begin(9600);   // Starts the serial port at 9600 baud
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);

  accelgyro.initialize();

  //digitalWrite(13, HIGH);
}

int val[6]; // 0-3 -> PADS
            // 4-5 -> ACCEL

void loop() {

  accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  
  val[0] = analogRead(A0);
  val[1] = analogRead(A1);
  val[2] = analogRead(A2);
  val[3] = analogRead(A3);
  
  val[4] = analogRead(A4);
  val[5] = analogRead(A5);

  //  Serial.print("0: ");
  //  Serial.println(val[0]);
  //  Serial.print("1: ");
  //  Serial.println(val[1]);
  //  Serial.print("2: ");
  //  Serial.println(val[2]);
  //  Serial.print("3: ");
  //  Serial.println(val[3]);

  // send pressure data
  Serial.print(" ");
  Serial.print(val[0]);
  Serial.print(",");
  Serial.print(val[1]);
  Serial.print(",");
  Serial.print(val[2]);
  Serial.print(",");
  Serial.print(val[3]);
  Serial.print(";");

  // send accel X,Y
  Serial.print(val[4]);
  Serial.print(",");
  Serial.print(val[5]);
  Serial.print(";");

  Serial.print(ax); Serial.print(",");
  Serial.print(ay); Serial.print(",");
  Serial.print(az); Serial.print(",");
  Serial.print(gx); Serial.print(",");
  Serial.print(gy); Serial.print(",");
  Serial.println(gz);

  for(int i=0; i<4; ++i){
    analogWrite( 6, map(val[i], 0, 1023, 0, 255) );
    analogWrite( 9, map(val[i], 0, 1023, 0, 255) );
    analogWrite(10, map(val[i], 0, 1023, 0, 255) );
    analogWrite(11, map(val[i], 0, 1023, 0, 255) );
  }

  delay(200);
}
