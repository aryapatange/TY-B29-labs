# Bayes Theorem Examples (Disease, Spam, Weather)

def bayes(prior, like_h, like_not_h):
    p_e = like_h*prior + like_not_h*(1-prior)
    return (like_h*prior)/p_e

# Example datasets (prior, likelihood_given_H, likelihood_given_not_H)
examples = {
    "Disease Detection" : (0.01, 0.95, 0.10),
    "Spam Detection"    : (0.30, 0.80, 0.05),
    "Rain Prediction"   : (0.20, 0.90, 0.30)
}

print("\nBayes Results:\n")

for name, (p, lh, lnh) in examples.items():
    post = bayes(p, lh, lnh)
    print(f"{name}: P(H|E) = {post:.4f}  | Confidence = {post*100:.2f}%")

