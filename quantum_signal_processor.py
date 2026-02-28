import math
import json
import hashlib
from typing import List

def collect_signal(samples: List[float]) -> List[float]:
    return samples

def normalize(signal: List[float]) -> List[float]:
    norm = math.sqrt(sum(x * x for x in signal))
    if norm == 0:
        raise ValueError("Invalid signal")
    return [x / norm for x in signal]

def compress_features(signal: List[float], max_features: int = 2) -> List[float]:
    return signal[:max_features]

def secure_payload(parameters: List[float]) -> dict:
    payload = json.dumps(parameters).encode()
    checksum = hashlib.sha256(payload).hexdigest()
    return {"params": parameters, "checksum": checksum}

def prepare_quantum_job(raw_signal: List[float]) -> dict:
    signal = collect_signal(raw_signal)
    normalized = normalize(signal)
    features = compress_features(normalized)
    return secure_payload(features)

if __name__ == "__main__":
    raw = [0.8, 0.3, 0.1]
    job = prepare_quantum_job(raw)
    print("Quantum Job:", job)