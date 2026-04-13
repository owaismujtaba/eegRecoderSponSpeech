from enum import Enum, auto

class Markers(Enum):
    START_EXPERIMENT = auto()
    END_EXPERIMENT = auto()
    START_RESTING = auto()
    END_RESTING = auto()
    START_FIXATION = auto()
    END_FIXATION = auto()
    START_DISPLAY_IMAGE = auto()
    END_DISPLAY_IMAGE = auto()


class MarkerConfig:
    MAPPING = {
        Markers.START_EXPERIMENT:          (255, 'StartExperiment'),
        Markers.END_EXPERIMENT:            (232, 'EndExperiment'),
        Markers.START_FIXATION:      (209, 'StartFixation'),
        Markers.END_FIXATION:            (196, 'EndFixation'),
        Markers.START_RESTING:       (163, 'StartResting'),
        Markers.END_RESTING:         (150, 'EndResting'),
        Markers.START_DISPLAY_IMAGE:   (140, 'StartDisplayImage'),
        Markers.END_DISPLAY_IMAGE: (117, 'EndDisplayImage'),
    }

    @staticmethod
    def get_command(marker_type):
        value, label = MarkerConfig.MAPPING.get(marker_type, (0, 'Unknown'))
        return f"WRITE {value} 20000 0\n".encode('utf-8'), label
