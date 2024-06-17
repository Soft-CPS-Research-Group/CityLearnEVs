{
  "root_directory": null,
  "central_agent": false,
  "simulation_start_time_step": 0,
  "simulation_end_time_step": 8759,
  "episodes": 1,
  "seconds_per_time_step": 3600,
  "observations": {
      "month": {
        "active": true,
        "shared_in_central_agent": true
      },
      "day_type": {
        "active": true,
        "shared_in_central_agent": true
      },
      "hour": {
        "active": true,
        "shared_in_central_agent": true
      },
      "daylight_savings_status": {
        "active": false,
        "shared_in_central_agent": true
      },
      "outdoor_dry_bulb_temperature": {
        "active": true,
        "shared_in_central_agent": true
      },
      "outdoor_dry_bulb_temperature_predicted_6h": {
        "active": true,
        "shared_in_central_agent": true
      },
      "outdoor_dry_bulb_temperature_predicted_12h": {
        "active": true,
        "shared_in_central_agent": true
      },
      "outdoor_dry_bulb_temperature_predicted_24h": {
        "active": true,
        "shared_in_central_agent": true
      },
      "outdoor_relative_humidity": {
        "active": true,
        "shared_in_central_agent": true
      },
      "outdoor_relative_humidity_predicted_6h": {
        "active": true,
        "shared_in_central_agent": true
      },
      "outdoor_relative_humidity_predicted_12h": {
        "active": true,
        "shared_in_central_agent": true
      },
      "outdoor_relative_humidity_predicted_24h": {
        "active": true,
        "shared_in_central_agent": true
      },
      "diffuse_solar_irradiance": {
        "active": true,
        "shared_in_central_agent": true
      },
      "diffuse_solar_irradiance_predicted_6h": {
        "active": true,
        "shared_in_central_agent": true
      },
      "diffuse_solar_irradiance_predicted_12h": {
        "active": true,
        "shared_in_central_agent": true
      },
      "diffuse_solar_irradiance_predicted_24h": {
        "active": true,
        "shared_in_central_agent": true
      },
      "direct_solar_irradiance": {
        "active": true,
        "shared_in_central_agent": true
      },
      "direct_solar_irradiance_predicted_6h": {
        "active": true,
        "shared_in_central_agent": true
      },
      "direct_solar_irradiance_predicted_12h": {
        "active": true,
        "shared_in_central_agent": true
      },
      "direct_solar_irradiance_predicted_24h": {
        "active": true,
        "shared_in_central_agent": true
      },
      "carbon_intensity": {
        "active": true,
        "shared_in_central_agent": true
      },
      "indoor_dry_bulb_temperature": {
        "active": false,
        "shared_in_central_agent": false
      },
      "average_unmet_cooling_setpoint_difference": {
        "active": false,
        "shared_in_central_agent": false
      },
      "indoor_relative_humidity": {
        "active": false,
        "shared_in_central_agent": false
      },
      "non_shiftable_load": {
        "active": true,
        "shared_in_central_agent": false
      },
      "solar_generation": {
        "active": true,
        "shared_in_central_agent": false
      },
      "cooling_storage_soc": {
        "active": false,
        "shared_in_central_agent": false
      },
      "heating_storage_soc": {
        "active": false,
        "shared_in_central_agent": false
      },
      "dhw_storage_soc": {
        "active": false,
        "shared_in_central_agent": false
      },
      "electrical_storage_soc": {
        "active": true,
        "shared_in_central_agent": false
      },
      "net_electricity_consumption": {
        "active": true,
        "shared_in_central_agent": false
      },
      "electricity_pricing": {
        "active": true,
        "shared_in_central_agent": false
      },
      "electricity_pricing_predicted_6h": {
        "active": true,
        "shared_in_central_agent": false
      },
      "electricity_pricing_predicted_12h": {
        "active": true,
        "shared_in_central_agent": false
      },
      "electricity_pricing_predicted_24h": {
        "active": true,
        "shared_in_central_agent": false
      },
      "ev_charger_state": {
        "active": true,
        "shared_in_central_agent": false
      },
      "ev_estimated_departure_time": {
        "active": true,
        "shared_in_central_agent": false
      },
      "ev_required_soc_departure": {
        "active": true,
        "shared_in_central_agent": false
      },
      "ev_estimated_arrival_time": {
        "active": true,
        "shared_in_central_agent": false
      },
      "ev_estimated_soc_arrival": {
        "active": true,
        "shared_in_central_agent": false
      },
      "ev_soc": {
        "active": true,
        "shared_in_central_agent": false
      }
  },
  "actions": {
      "cooling_storage": {
        "active": false
      },
      "heating_storage": {
        "active": false
      },
      "dhw_storage": {
        "active": false
      },
      "electrical_storage": {
        "active": true
      },
      "ev_storage": {
        "active": true
      }
  },
  "agent": {
    "type": "citylearn.agents.sac.SAC",
    "attributes": {
      "hidden_dimension": [
        256,
        256
      ],
      "discount": 0.99,
      "tau": 0.005,
      "lr": 0.003,
      "batch_size": 256,
      "replay_buffer_capacity": 100000.0,
      "standardize_start_time_step": 6000,
      "end_exploration_time_step": 7000,
      "action_scaling_coef": 0.5,
      "reward_scaling": 5.0,
      "update_per_time_step": 2
    }
  },
  "reward_function": {
    "type": "citylearn.reward_function.MARL",
    "attributes": {
    }
  },
  "evs": {
    "EV_1": {
      "include": true,
      "energy_simulation": "EV_1.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "image_path": "images/ev.png",
      "battery": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 40,
          "nominal_power": 50,
          "initial_soc": 0.25
        }
      }
    },
    "EV_2": {
      "include": true,
      "energy_simulation": "EV_2.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "image_path": "images/ev.png",
      "battery": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 50,
          "nominal_power": 50,
          "initial_soc": 0.35
        }
      }
    },
    "EV_3": {
      "include": true,
      "energy_simulation": "EV_3.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "image_path": "images/ev.png",
      "battery": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 75,
          "nominal_power": 50,
          "initial_soc": 0.5
        }
      }
    },
    "EV_4": {
      "include": true,
      "energy_simulation": "EV_4.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "image_path": "images/ev.png",
      "battery": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 45,
          "nominal_power": 50,
          "initial_soc": 0.2
        }
      }
    },
    "EV_5": {
      "include": true,
      "energy_simulation": "EV_5.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "image_path": "images/ev.png",
      "battery": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 90,
          "nominal_power": 50,
          "initial_soc": 0.8
        }
      }
    },
    "EV_6": {
      "include": true,
      "energy_simulation": "EV_6.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "image_path": "images/ev.png",
      "battery": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 100,
          "nominal_power": 50,
          "initial_soc": 0.8
        }
      }
    },
    "EV_7": {
      "include": true,
      "energy_simulation": "EV_7.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "image_path": "images/ev.png",
      "battery": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 60,
          "nominal_power": 50,
          "initial_soc": 0.1
        }
      }
    },
    "EV_8": {
      "include": true,
      "energy_simulation": "EV_8.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "image_path": "images/ev.png",
      "battery": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 80,
          "nominal_power": 50,
          "initial_soc": 0.2
        }
      }
    }
  },
  "buildings": {
    "Building_1": {
      "include": true,
      "energy_simulation": "Building_1.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "coordinates": {
        "latitude": 41.195632,
        "longitude": -8.598365
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "inactive_observations": [],
      "inactive_actions": [],
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 12.0
        }
      },
      "chargers": {
        "charger_1_1": {
          "type": "citylearn.electric_vehicle_charger.Charger",
          "autosize": false,
          "image_path": "images/charger.png",
          "attributes": {
            "nominal_power": 11,
            "efficiency": 0.95,
            "charger_type": 0,
            "max_charging_power": 11,
            "min_charging_power": 1.4,
            "max_discharging_power": 7.2,
            "min_discharging_power": 0.0
          }
        }
      }
    },
    "Building_2": {
      "include": true,
      "energy_simulation": "Building_2.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 4.0
        }
      }
    },
    "Building_3": {
      "include": true,
      "energy_simulation": "Building_3.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 4.0
        }
      }
    },
    "Building_4": {
      "include": true,
      "energy_simulation": "Building_4.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "coordinates": {
        "latitude": 41.189875,
        "longitude": -8.612208
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "inactive_observations": [],
      "inactive_actions": [],
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 8.0
        }
      },
      "chargers": {
        "charger_4_1": {
          "type": "citylearn.electric_vehicle_charger.Charger",
          "autosize": false,
          "image_path": "images/charger.png",
          "attributes": {
            "nominal_power": 22,
            "efficiency": 0.95,
            "charger_type": 1,
            "max_charging_power": 22,
            "min_charging_power": 3.7,
            "max_discharging_power": 22,
            "min_discharging_power": 3.7
          }
        }
      }
    },
    "Building_5": {
      "include": true,
      "energy_simulation": "Building_5.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "coordinates": {
        "latitude": 41.202139,
        "longitude": -8.644700
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "inactive_observations": [],
      "inactive_actions": [],
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 10.0
        }
      },
      "chargers": {
        "charger_5_1": {
          "type": "citylearn.electric_vehicle_charger.Charger",
          "autosize": false,
          "image_path": "images/charger.png",
          "attributes": {
            "nominal_power": 7.4,
            "efficiency": 0.95,
            "charger_type": 1,
            "max_charging_power": 7.4,
            "min_charging_power": 0,
            "max_discharging_power": 7.4,
            "min_discharging_power": 0
          }
        }
      }
    },
    "Building_6": {
      "include": true,
      "energy_simulation": "Building_6.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "inactive_observations": [],
      "inactive_actions": [],
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 4.0
        }
      }
    },
    "Building_7": {
      "include": true,
      "energy_simulation": "Building_7.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 9.0
        }
      },
      "chargers": {
        "charger_7_1": {
          "type": "citylearn.electric_vehicle_charger.Charger",
          "autosize": false,
          "image_path": "images/charger.png",
          "attributes": {
            "nominal_power": 11,
            "efficiency": 0.90,
            "charger_type": 1,
            "max_charging_power": 11,
            "min_charging_power": 0,
            "max_discharging_power": 11,
            "min_discharging_power": 0
          }
        }
      }
    },
    "Building_8": {
      "include": true,
      "energy_simulation": "Building_8.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 4.0
        }
      }
    },
    "Building_9": {
      "include": true,
      "energy_simulation": "Building_9.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 4.0
        }
      }
    },
    "Building_10": {
      "include": true,
      "energy_simulation": "Building_10.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 6.0
        }
      },
      "chargers": {
        "charger_10_1": {
          "type": "citylearn.electric_vehicle_charger.Charger",
          "autosize": false,
          "image_path": "images/charger.png",
          "attributes": {
            "nominal_power": 7.4,
            "efficiency": 0.95,
            "charger_type": 1,
            "max_charging_power": 7.4,
            "min_charging_power": 0,
            "max_discharging_power": 7.4,
            "min_discharging_power": 0
          }
        }
      }
    },
    "Building_11": {
      "include": true,
      "energy_simulation": "Building_11.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 5.0
        }
      }
    },
    "Building_12": {
      "include": true,
      "energy_simulation": "Building_12.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 8.0
        }
      },
      "chargers": {
        "charger_12_1": {
          "type": "citylearn.electric_vehicle_charger.Charger",
          "autosize": false,
          "image_path": "images/charger.png",
          "attributes": {
            "nominal_power": 7.4,
            "efficiency": 0.95,
            "charger_type": 1,
            "max_charging_power": 7.4,
            "min_charging_power": 0,
            "max_discharging_power": 7.4,
            "min_discharging_power": 0
          }
        }
      }
    },
    "Building_13": {
      "include": true,
      "energy_simulation": "Building_13.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 5.0
        }
      }
    },
    "Building_14": {
      "include": true,
      "energy_simulation": "Building_14.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 5.0
        }
      }
    },
    "Building_15": {
      "include": true,
      "energy_simulation": "Building_15.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 15.0
        }
      },
      "chargers": {
        "charger_15_1": {
          "type": "citylearn.electric_vehicle_charger.Charger",
          "autosize": false,
          "image_path": "images/charger.png",
          "attributes": {
            "nominal_power": 7.4,
            "efficiency": 0.95,
            "charger_type": 1,
            "max_charging_power": 7.4,
            "min_charging_power": 0,
            "max_discharging_power": 7.4,
            "min_discharging_power": 0
          }
        },
        "charger_15_2": {
          "type": "citylearn.electric_vehicle_charger.Charger",
          "autosize": false,
          "image_path": "images/charger.png",
          "attributes": {
            "nominal_power": 11,
            "efficiency": 0.95,
            "charger_type": 1,
            "max_charging_power": 11,
            "min_charging_power": 0,
            "max_discharging_power": 11,
            "min_discharging_power": 0
          }
        }
      }
    },
    "Building_16": {
      "include": true,
      "energy_simulation": "Building_16.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 5.0
        }
      }
    },
    "Building_17": {
      "include": true,
      "energy_simulation": "Building_17.csv",
      "weather": "weather.csv",
      "carbon_intensity": "carbon_intensity.csv",
      "pricing": "pricing.csv",
      "inactive_observations": [],
      "inactive_actions": [],
      "coordinates": {
        "latitude": 41.209114,
        "longitude":  -8.632814
      },
      "image_path": "images/building.png",
      "reward_type": "D",
      "electrical_storage": {
        "type": "citylearn.energy_model.Battery",
        "autosize": false,
        "attributes": {
          "capacity": 6.4,
          "efficiency": 0.9,
          "capacity_loss_coefficient": 1e-05,
          "loss_coefficient": 0.0,
          "nominal_power": 5.0
        }
      },
      "pv": {
        "type": "citylearn.energy_model.PV",
        "autosize": false,
        "attributes": {
          "nominal_power": 5.0
        }
      }
    }
  }
}