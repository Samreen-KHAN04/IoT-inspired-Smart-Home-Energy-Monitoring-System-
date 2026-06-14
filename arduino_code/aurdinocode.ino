#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SENSOR_PIN 34
#define LED_PIN 2
#define BUZZER_PIN 15

Adafruit_SSD1306 display(128, 64, &Wire, -1);

void setup() {

  Serial.begin(115200);

  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  if(!display.begin(
      SSD1306_SWITCHCAPVCC,
      0x3C))
  {
    while(true);
  }

  display.clearDisplay();
}

void loop() {

  int sensorValue =
      analogRead(SENSOR_PIN);

  float current =
      map(sensorValue,
          0,
          4095,
          0,
          30);

  float voltage = 230.0;

  float power =
      voltage * current;

  Serial.print("Current: ");
  Serial.print(current);

  Serial.print(" A | Power: ");
  Serial.print(power);

  Serial.println(" W");

  display.clearDisplay();

  display.setTextSize(1);
  display.setTextColor(WHITE);

  display.setCursor(0,0);
  display.print("Current:");
  display.println(current);

  display.print("Power:");
  display.println(power);

  display.display();

  if(power > 1000)
  {
    digitalWrite(LED_PIN, HIGH);

    tone(BUZZER_PIN, 1000);
  }
  else
  {
    digitalWrite(LED_PIN, LOW);

    noTone(BUZZER_PIN);
  }

  delay(2000);
}