# cherry-picker

**Smart IP selection tool for penetration testers.**

Cherry Picker helps you prioritize and cherry-pick IP addresses for scanning, based on real-world heuristics, entropy, clustering, TTL, and cloud targeting — to scan smarter, not harder.

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

```bash
git clone https://github.com/mev0lent/cherry-picker.git
cd cherry-picker
pip install .
```

Or in dev mode:

```bash
pip install -e .
```

> ⚠️ Requires Python 3.8+

---

## 🚀 Usage

```bash
cherry-picker pick 192.168.1.0/24 --strategy first_octet_bias --count 30
```

### Combinations

```bash
cherry-picker pick 10.0.0.0/16 --strategy "cloud_patterns:0.6+random:0.4"
```

### With live ping check

```bash
cherry-picker pick 192.168.0.0/24 --strategy entropy_reduce --ping-check
```

### Using input files

```bash
cherry-picker pick 10.0.0.0/16 --strategy cluster_focus --input-file alive_hosts.txt
cherry-picker pick 192.168.1.0/24 --strategy ttl_clustering --input-file ttl_data.txt
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

