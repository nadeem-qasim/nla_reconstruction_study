# Deletion Gap of Reconstruction in Natural Language Autoencoders is in the Final Explanation Sentence

## Abstract

AIs monitoring, reporting or restricting other AIs is a really interesting direction in control research. This can be done on several levels. For instance, behavior (what actions the AI is taking), reasoning traces (what's the AI thinking out loud), and white box (what's the AI's thinking internally).

Natural language autoencoders ([NLAs](https://transformer-circuits.pub/2026/nla/)) are an interesting thing in the third category. They explain in natural language an LLM's internal thoughts (more precisely activation at a particular layer at a particular token). An issue is the explanation can contain hallucinations.

NLAs are trained unsupervised with an encoder-decoder setup. The encoder converts the activation to natural language, the decoder converts back to an activation, and the reconstruction error drives the training.

The paper found that a larger mean drop in fraction of variance explained (FVE), so worse reconstruction, occurs from deleting true claims than false claims. This could be a useful monitor if usable to filter individual claims.

I ran experiments on two open NLAs (Qwen2.5-7B Layer 20 and Qwen3.6-27B Layer 42) with the following findings

1. despite mean deletion gap, individual claim discrimination is weak for 7B, and a coin flip for 27B (AUROC near 0.5)

2. claims associated with the final sentence have better discrimination (0.67 and 0.70 AUROC)

3. paraphrasing (syntax changed, semantics held constant) does not add additional discriminative value

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1793502373/lexical_client_uploads/rcyguljicpbpmk3zelpg.png)

## Main result

- **Data:** 100 Re-DocRED Wikipedia introductions, each cut at a word boundary; the activation is read at its final token
- **Claims:** explanations are split into atomic true, false, and irrelevant claims against the prefix and Re-DocRED annotations; see [the annotation guide](https://fve_claims/ANNOTATION_GUIDE.md).
- **Edits:** deletions remove exact claim text spans, and paraphrases rewrite a sentence preserving semantics
- **Analysis:** calculate FVE-drop per claim and means, confidence intervals, per-claim AUROC, claims labeled with category (theme, entity, detail) and position (final sentence or not)

For each final-token activation, NLA explanations are generated, split into atomic claims, labeled using an LLM-as-judge with the source text as reference (I hand-checked 15+ randomized <text,claim> pairs with 1 disagreement).

The FVE is measured after deleting each claim, and the percentage points (**pp**) change is recorded.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1793501250/lexical_client_uploads/vr3pf5hhcghzy0ktutxc.png)

AUROC tells us how well the FVE separate the claims; for a random pair of true and false claim, the probability that the true claim has a larger FVE drop.


| model                 | mean drop, true / false (pp) | AUROC (95% CI)       |
| --------------------- | ---------------------------- | -------------------- |
| Qwen2.5-7B, layer 20  | 1.58 / 0.94                  | 0.581 [0.551, 0.613] |
| Qwen3.6-27B, layer 42 | 4.15 / 2.66                  | 0.490 [0.451, 0.529] |


So deletion reproduces the mean FVE gap between true and false claims. However individual discrimination is weak (7B) or near chance (27B)

I also experimented with paraphrasing; it did not improve discrimination. The 27B's mean drop was 0.09 **pp** and 0.20 **pp** for true and false claims respectively, and 17 **pp** mean drop for either claim type for 7B. Combining paraphrase and deletion drops using logistic regression did not improve AUROC.

Claim category (theme, entity, or detail) effects mirrored the original paper's result. Results on 27B:

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1793502323/lexical_client_uploads/ukykfzca7xeikg9cnj5a.png)

## Final explanation sentence carries most of the signal

The mean true-false gap is concentrated in claims in the final explanation sentence, which typically describe the activation site or source ending.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1793501657/lexical_client_uploads/goa4lavrondfvjmkzha5.png)

## Alternative explanations and limitations

- Only two models tested with max 27B parameters; phenomena may differ at scale and on other model families
- Dataset is artificial and limited in size, 100 wikipedia articles with roughly 1200 claims evaluated per model
- The original NLA paper used different models (Haiku, Opus), and didn't report breakdown by explanation sentence Differences in activation site location, or claim-extraction and labeling method could also explain the difference

## Related Work

While doing the write up, I came across following works.

- Shorter NLA explanations ([https://www.lesswrong.com/posts/NazprRfWJ4qkwcSro/nla-explanations-can-be-shortened-without-harming](https://www.lesswrong.com/posts/NazprRfWJ4qkwcSro/nla-explanations-can-be-shortened-without-harming)): substantially shorter explanations can retain reconstruction quality
- Three Pieces of Evidence that the NLA Reconstructor Does Not Read Semantics or Syntax ([https://www.lesswrong.com/posts/Q5fwBiZCwHGeKucmo/three-pieces-of-evidence-that-the-nla-reconstructor-does-not](https://www.lesswrong.com/posts/Q5fwBiZCwHGeKucmo/three-pieces-of-evidence-that-the-nla-reconstructor-does-not)): reconstruction responds poorly to changes in meaning and grammar
- Train the Model, Not the Reader ([https://arxiv.org/abs/2607.20379](https://arxiv.org/abs/2607.20379)): good reconstruction need not validate individual claims
- Training activation verbalizers to front-load reconstruction-relevant information ([https://www.lesswrong.com/posts/aWYQHh2pEFCLYh85C/matryoshka-nlas-training-activation-verbalizers-to-frontload-1](https://www.lesswrong.com/posts/aWYQHh2pEFCLYh85C/matryoshka-nlas-training-activation-verbalizers-to-frontload-1)): randomly truncating explanations during training makes the NLA front-load the most reconstruction sensitive claims, though FVE did not help filter hallucinations



## Table of Content


| path                       | what                                                                                |
| -------------------------- | ----------------------------------------------------------------------------------- |
| `fve_claims/`              | claims, labels, edits, scores, analysis                                             |
| `fve_claims/analysis_27b/` | script per reported number                                                          |
| `fve_claims/audit/`        | blind label check, sheet and key                                                    |
|                            |                                                                                     |
| `src/`, `scripts/`         | 7B NLA library and model loader; dataset builder and checkpoint setup for both NLAs |
| `PROVENANCE.md`            | human and AI division of labor                                                      |


Research question, decisions, manual checks, and writing are mine. 
AI did most of the coding, assisted analyses, feedback on writing, and summarized existing work. 