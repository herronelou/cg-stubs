# mypy: disable-error-code="misc, override, no-redef"

class ConfigController:
    def __init__(self, currentConfig, appController): ...
    def _hide(self, ui): ...
    def _saveAsTriggered(self): ...
    def _validateAndSaveConfig(self, newName, dialog): ...
    def reloadConfigController(self): ...