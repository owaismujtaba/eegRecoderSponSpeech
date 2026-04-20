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
        Markers.START_EXPERIMENT:          (250, 'StartExperiment'),
        Markers.END_EXPERIMENT:            (230, 'EndExperiment'),
        Markers.START_FIXATION:      (200, 'StartFixation'),
        Markers.END_FIXATION:            (190, 'EndFixation'),
        Markers.START_RESTING:       (100, 'StartResting'),
        Markers.END_RESTING:         (90, 'EndResting'),
        Markers.START_DISPLAY_IMAGE:   (150, 'StartDisplayImage'),
        Markers.END_DISPLAY_IMAGE: (140, 'EndDisplayImage'),
    }

    @staticmethod
    def get_command(marker_type):
        value, label = MarkerConfig.MAPPING.get(marker_type, (0, 'Unknown'))
        return f"WRITE {value} 20000 0\n".encode('utf-8'), label
