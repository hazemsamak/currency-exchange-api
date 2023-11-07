import shutil


class DiskUsageClient:
    def get_disk_space(self):
        BytesPerGB = 1024 * 1024 * 1024
        (total, used, free) = shutil.disk_usage("/")
        internal_usage = {
            "total": "%.0f GB" % (float(total)/BytesPerGB),
            "used": "%.0f GB" % (float(used)/BytesPerGB),
            "free": "%.0f GB" % (float(free)/BytesPerGB),
            "free_perc": "%.0f" % (float(free)/float(total)*100)+"%"
        }
        (total, used, free) = shutil.disk_usage("/media/external")
        external_usage = {
            "total": "%.0f GB" % (float(total)/BytesPerGB),
            "used": "%.0f GB" % (float(used)/BytesPerGB),
            "free": "%.0f GB" % (float(free)/BytesPerGB),
            "free_perc": "%.0f" % (float(free)/float(total)*100)+"%"
        }
        usage = {
            "internal": internal_usage,
            "external": external_usage
        }
        return usage


diskUsageClient = DiskUsageClient()
print(diskUsageClient.get_disk_space())
