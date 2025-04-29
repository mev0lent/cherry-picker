# cherry-picker

**Smart IP selection tool for penetration testers.**

Cherry Picker helps you prioritize and cherry-pick IP addresses for scanning, based on real-world heuristics, entropy, clustering, TTL, and cloud targeting — to scan smarter, not harder.

---

## ⚠️ Disclaimer

This tool was developed during my studies at **University of Applied Sciences Mannheim** as part of a cybersecurity course.  
It is provided **for educational purposes only**.

**📌 No liability is assumed for any misuse or damage resulting from the use of this tool.**  
You are solely responsible for ensuring that any scan or interaction with a network complies with all applicable laws and regulations.

Never scan systems or networks without **explicit permission**.

---

## ✨ Features

- ✅ Random and heuristic sampling
- 🎯 Cloud-aware targeting (AWS, Azure, GCP)
- 🧠 Entropy-based filtering (avoid noisy IPs)
- ⏱ TTL clustering from real-world ping data
- 📡 Cluster expansion around known hits
- ⚙️ Combinable strategies (e.g. `random+entropy_reduce:0.5`)
- ⚡ Async high-speed ping checks
- 📄 Output as structured reports

---

## 📦 Installation

> ⚠️ Requires Python 3.8+

### 🔒 Recommended: Virtual Environment

To keep your system clean and isolated:

```bash
# Install virtualenv if needed
pip install virtualenv

# Create and activate environment
virtualenv -p python3 cherry-picker-env
source cherry-picker-env/bin/activate
```

### 🚀 Install Cherry Picker

Clone the repo and install:

```bash
git clone https://github.com/yourusername/cherry-picker.git #or via ssh
cd cherry-picker
pip install .
```

Or for development mode (auto reload when editing):

```bash
pip install -e .
```

---

## 🚀 Usage

```bash
cherry-picker --strategy first_octet_bias --count 30 192.168.1.0/24
```

### Combinations

```bash
cherry-picker --strategy "cloud_patterns:0.6+random:0.4" 10.0.0.0/16
```

### With live ping check

```bash
cherry-picker 192.168.0.0/24 --strategy entropy_reduce --ping-check
```

### Using input files

```bash
cherry-picker --strategy cluster_focus --input-file alive_hosts.txt 10.0.0.0/16 
cherry-picker --strategy ttl_clustering --input-file ttl_data.txt 192.168.1.0/24
```

---

## 📤 Output

Save a structured report:

```bash
--output-file report.txt
```

Format:
```
# Cherry Picker Report
# CIDR: 192.168.1.0/24
# Strategy: entropy_reduce
# Ping Check: enabled
# Total Alive Hosts: 9

192.168.1.1
192.168.1.10
...
```

---

## 🤖 Supported Strategies

| Name               | Description |
|--------------------|-------------|
| `random`           | Pure random selection |
| `heuristic`        | Picks common infra IPs (e.g. `.1`, `.10`) |
| `first_octet_bias` | Focus on IPs with interesting suffixes |
| `cluster_focus`    | Expands near known IPs (requires input) |
| `cloud_patterns`   | Targets AWS, Azure, GCP address space |
| `entropy_reduce`   | Picks low-entropy, structured IPs |
| `ttl_clustering`   | Groups IPs with similar TTLs (requires input) |

---

## 🔧 Dev & Testing

You can use your own `.txt` files for IP and TTL input:

- `alive_hosts.txt`: One IP per line
- `ttl_data.txt`: Format `IP TTL`, one per line

---

## 💡 Roadmap Ideas

- Add CSV/JSON export
- Auto-detect cloud IPs from online sources
- Passive recon integration

---

## 🧑‍💻 Author

Made with ❤️ by [Niklas Heringer](https://niklas-heringer.com)
```

