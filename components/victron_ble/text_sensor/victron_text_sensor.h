#pragma once

#include "esphome/components/text_sensor/text_sensor.h"
#include "esphome/components/victron_ble/victron_ble.h"

namespace esphome {
namespace victron_ble {

enum class VICTRON_TEXT_SENSOR_TYPE {
  ALARM,
  ACTIVE_AC_IN,
  ALARM_REASON,
  CHARGER_ERROR,
  DEVICE_STATE,
  ERROR_CODE,
  OFF_REASON,
  WARNING_REASON,
};

class VictronTextSensor : public Component, public text_sensor::TextSensor, public Parented<VictronBle> {
 public:
  void dump_config() override;
  void setup() override;

  void set_type(VICTRON_TEXT_SENSOR_TYPE val) { this->type_ = val; }

 protected:
  VICTRON_TEXT_SENSOR_TYPE type_;

  void publish_state_(VE_REG_ALARM_REASON val);
  void publish_state_(VE_REG_DEVICE_STATE val);
  void publish_state_(VE_REG_CHR_ERROR_CODE val);
  void publish_state_(VE_REG_DEVICE_OFF_REASON_2 val);
  void publish_state_(VE_REG_AC_IN_ACTIVE val);
  void publish_state_(VE_REG_ALARM_NOTIFICATION val);
};
}  // namespace victron_ble
}  // namespace esphome