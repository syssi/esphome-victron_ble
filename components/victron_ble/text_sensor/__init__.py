from esphome.components import text_sensor
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import (
    CONF_TYPE,
)
from .. import victron_ble_ns, CONF_VICTRON_BLE_ID, VictronBle

DEPENDENCIES = ["victron_ble"]
CODEOWNERS = ["@Fabian-Schmidt"]

VictronTextSensor = victron_ble_ns.class_(
    "VictronTextSensor", text_sensor.TextSensor, cg.Component)

VICTRON_TEXT_SENSOR_TYPE = victron_ble_ns.namespace(
    "VICTRON_TEXT_SENSOR_TYPE")

CONF_SUPPORTED_TYPE = {
    "ALARM":  {
        CONF_TYPE: VICTRON_TEXT_SENSOR_TYPE.ALARM,
    },
    "ACTIVE_AC_IN":  {
        CONF_TYPE: VICTRON_TEXT_SENSOR_TYPE.ACTIVE_AC_IN,
    },
    "ALARM_REASON":  {
        CONF_TYPE: VICTRON_TEXT_SENSOR_TYPE.ALARM_REASON,
    },
    "CHARGER_ERROR":  {
        CONF_TYPE: VICTRON_TEXT_SENSOR_TYPE.CHARGER_ERROR,
    },
    "DEVICE_STATE":  {
        CONF_TYPE: VICTRON_TEXT_SENSOR_TYPE.DEVICE_STATE,
    },
    "ERROR_CODE":  {
        CONF_TYPE: VICTRON_TEXT_SENSOR_TYPE.ERROR_CODE,
    },
    "OFF_REASON":  {
        CONF_TYPE: VICTRON_TEXT_SENSOR_TYPE.OFF_REASON,
    },
    "WARNING_REASON":  {
        CONF_TYPE: VICTRON_TEXT_SENSOR_TYPE.WARNING_REASON,
    },
}


CONFIG_SCHEMA = (
    text_sensor.text_sensor_schema(VictronTextSensor)
    .extend({
        cv.GenerateID(CONF_VICTRON_BLE_ID): cv.use_id(VictronBle),
        cv.Required(CONF_TYPE): cv.enum(CONF_SUPPORTED_TYPE, upper=True),
    }).extend(cv.COMPONENT_SCHEMA)
)


async def to_code(config):
    var = await text_sensor.new_text_sensor(config)
    await cg.register_component(var, config)
    await cg.register_parented(var, config[CONF_VICTRON_BLE_ID])

    cg.add(var.set_type(CONF_SUPPORTED_TYPE[config[CONF_TYPE]][CONF_TYPE]))
