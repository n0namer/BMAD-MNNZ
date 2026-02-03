   ├─ Conduct pairwise comparisons
   ├─ Calculate weights
   ├─ Check consistency (CR < 0.10)
   └─ If inconsistent → revise comparisons

3. Score Alternatives on Each Criterion
   ├─ Use 1-10 scale or quantitative metrics
   ├─ Specify benefit vs cost for each criterion
   └─ Build m×n decision matrix

4. Run TOPSIS for Rankings
   ├─ Normalize decision matrix
   ├─ Apply AHP weights
   ├─ Calculate Ci scores
   └─ Rank alternatives (highest Ci = best)

5. Validate & Decide
   ├─ Run sensitivity analysis
   ├─ Check if top 2-3 alternatives are clearly separated
   ├─ Review qualitative factors (not in model)
   └─ Make final decision

6. Document & Monitor
   ├─ Record AHP matrix and weights
   ├─ Track Ci scores over time
   ├─ Set triggers for recalculation
   └─ Update when new projects or data emerge
```

---

## Part 6: References & Further Reading

### Academic Foundations
1. Saaty, T. L. (1980). *The Analytic Hierarchy Process*. McGraw-Hill.
2. Hwang, C. L., & Yoon, K. (1981). *Multiple Attribute Decision Making: Methods and Applications*. Springer.
3. Tzeng, G. H., & Huang, J. J. (2011). *Multiple Attribute Decision Making: Methods and Applications*. CRC Press.

### Practical Guides
- Alonso, J. A., & Lamata, M. T. (2006). "Consistency in the Analytic Hierarchy Process: A New Approach." *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems*, 14(4), 445-459.
- Behzadian, M., et al. (2012). "A state-of-the-art survey of TOPSIS applications." *Expert Systems with Applications*, 39(17), 13051-13069.

### Online Resources
- [AHP Online Calculator](https://bpmsg.com/ahp/)
- [TOPSIS Tutorial with Excel](https://www.youtube.com/watch?v=example)
- [Decision Analysis Society](https://www.informs.org/Community/DAS)

---

## Appendix: Quick Reference Tables

### AHP Pairwise Comparison Scale
| Score | Meaning | When to Use |
|-------|---------|-------------|
| 1 | Equal | Criteria contribute equally |
| 3 | Moderate | Slight favor based on experience |
| 5 | Strong | Strong favor based on evidence |
| 7 | Very strong | Clear dominance demonstrated |
| 9 | Extreme | Highest possible evidence |

### Random Index (RI) for Consistency
| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|-----|
| RI| 0 | 0 |0.58|0.90|1.12|1.24|1.32|1.41|1.45|1.49|

### Criterion Type Classification
| Criterion | Type | TOPSIS Ideal |
|-----------|------|--------------|
| Impact on goals | Benefit | Maximum |
| Effort required | Cost | Minimum |
| Risk level | Cost | Minimum |
| Timeline (days) | Cost | Minimum |
| ROI | Benefit | Maximum |
| Quality score | Benefit | Maximum |
| Complexity | Cost | Minimum |
| Stakeholder support | Benefit | Maximum |

---

*Last Updated: 2026-02-01*
*Version: 1.0*
*Author: MCDA Framework Working Group*
