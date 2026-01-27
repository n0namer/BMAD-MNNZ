# BMAD Compliance Fixes Todo (на основе validation-report-20260124-1917.md)
- [ ] Декомпозировать крупные step-файлы (разбить >250 строк/файл), справочные блоки вынести в data/
- [ ] В каждый step-файл добавить frontmatter по BMAD (`name`, `description`, пути, структурные переменные)
- [ ] Использовать переменные в теле по шаблону `{var}` вместо `${var}` и других нестандартных конструкций
- [ ] Реализовать BMAD-меню: display секция, handler, execution rules, redisplay, с буквенными опциями
- [ ] Все шаги привести к паттернам init/middle/final/validation/edit (см. step-type-patterns.md)
- [ ] Во всех шагах оформить OUTPUT секции по BMAD-шаблону (формат блока, описание выходных данных)
- [ ] Разметить struct/sequence связи между файлами, добавить traceability между outputs и inputs разных шагов
- [ ] Вынести повторяющиеся подпроцессы, проверки и шаблоны в отдельные модули, интегрировать factorization
- [ ] Ввести блоки recovery/fault tolerance/checkpointing, добавить explicit return points
- [ ] Во всех шагах создать acceptance/expected/checklist секции с критериями и чеклистами результата
- [ ] Уточнить архитектурную связность, явно обозначить linking между шагами/outputs/inputs
- [ ] Провести gap-analysis по coverage основного workflow и orchestration pipeline
- [ ] Автоматизировать roadmap и enforce структуру/навигацию через автогенерацию оглавлений
- [ ] Проверить/создать формализованные approval, review-team, peer-review блоки для командной работы

**ВНИМАНИЕ:** Исполнение этого чеклиста критически необходимо для получения статуса BMAD-compliant!