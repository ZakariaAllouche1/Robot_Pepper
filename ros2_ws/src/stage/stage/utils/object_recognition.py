def process_detections(labels, scores, centers, dt):
    return {
        "n": len(labels),
        "labels": labels,
        "scores": scores,
        "centers": centers,
        "latency_ms": round(dt, 1)
    }
