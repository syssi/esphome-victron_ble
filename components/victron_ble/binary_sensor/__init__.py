from esphome.components import binary_sensor
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import (
    CONF_TYPE,
)
from .. import victron_ble_ns, CONF_VICTRON_BLE_ID, VictronBle

DEPENDENCIES = ["victron_ble"]
CODEOWNERS = ["@Fabian-Schmidt"]

VictronBinarySensor = victron_ble_ns.class_(
    "VictronBinarySensor", binary_sensor.BinarySensor, cg.Component)

VICTRON_BINARY_SENSOR_TYPE = victron_ble_ns.namespace(
    "VICTRON_BINARY_SENSOR_TYPE")

CONF_SUPPORTED_TYPE = {
    "ALARM":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.ALARM,
    },
    "CHARGER_ERROR":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.CHARGER_ERROR,
    },
    "DEVICE_STATE_OFF":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_OFF,
    },
    "DEVICE_STATE_LOW_POWER":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_LOW_POWER,
    },
    "DEVICE_STATE_FAULT":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_FAULT,
    },
    "DEVICE_STATE_BULK":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_BULK,
    },
    "DEVICE_STATE_ABSORPTION":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_ABSORPTION,
    },
    "DEVICE_STATE_FLOAT":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_FLOAT,
    },
    "DEVICE_STATE_STORAGE":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_STORAGE,
    },
    "DEVICE_STATE_EQUALIZE_MANUAL":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_EQUALIZE_MANUAL,
    },
    "DEVICE_STATE_INVERTING":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_INVERTING,
    },
    "DEVICE_STATE_POWER_SUPPLY":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_POWER_SUPPLY,
    },
    "DEVICE_STATE_STARTING_UP":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_STARTING_UP,
    },
    "DEVICE_STATE_REPEATED_ABSORPTION":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_REPEATED_ABSORPTION,
    },
    "DEVICE_STATE_AUTO_EQUALIZE":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_AUTO_EQUALIZE,
    },
    "DEVICE_STATE_BATTERY_SAFE":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_BATTERY_SAFE,
    },
    "DEVICE_STATE_EXTERNAL_CONTROL":  {
        CONF_TYPE: VICTRON_BINARY_SENSOR_TYPE.DEVICE_STATE_EXTERNAL_CONTROL,
    },
}


CONFIG_SCHEMA = (
    binary_sensor.binary_sensor_schema(VictronBinarySensor)
    .extend({
        cv.GenerateID(CONF_VICTRON_BLE_ID): cv.use_id(VictronBle),
        cv.Required(CONF_TYPE): cv.enum(CONF_SUPPORTED_TYPE, upper=True),
    }).extend(cv.COMPONENT_SCHEMA)
)


async def to_code(config):
    var = await binary_sensor.new_binary_sensor(config)
    await cg.register_component(var, config)
    await cg.register_parented(var, config[CONF_VICTRON_BLE_ID])

    cg.add(var.set_type(CONF_SUPPORTED_TYPE[config[CONF_TYPE]][CONF_TYPE]))
