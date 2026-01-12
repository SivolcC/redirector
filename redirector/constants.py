"""Constants used throughout the redirector application."""

# Hosts file configuration
HOSTS_FILE_PATH = "/etc/hosts"
REDIRECTOR_BEGIN_MARKER = "# BEGIN REDIRECTOR MANAGED BLOCK\n"
REDIRECTOR_END_MARKER = "# END REDIRECTOR MANAGED BLOCK\n"

# Default configuration values
DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_LOG_FORMAT = "%(asctime)s :: %(levelname)s :: %(message)s"
DEFAULT_LOG_FILE_PATH = "/var/log/redirector.log"
DEFAULT_LOG_FILE_MAX_BYTES = 5000000
DEFAULT_LOG_FILE_MAX_BACKUPS = 5
DEFAULT_LB_CONFIGS_DIR = "lb_configs"
DEFAULT_PERSIST_HOSTS_BLOCK = True
DEFAULT_PID_FILE = None

# Healthcheck defaults
DEFAULT_TCP_TIMEOUT = 10.0
DEFAULT_HTTP_METHOD = "GET"
DEFAULT_HTTP_SCHEME = "http"
