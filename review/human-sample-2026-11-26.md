# Card translation reading sheet

Sample of 20 imported cards, drawn at random within strata (seed 20261126) from the 1492 cards imported at lean-pokemon `05a38b3`.
For each card: read the printed text, read the Lean term, and mark a verdict.

- **Right**: the term does what the card says, apart from the listed caveats and the global departures and readings (Known gaps, top of `Pokemon/Rules.lean`).
- **Wrong**: the term does something the card does not, or omits something, and no listed caveat covers it.
- **Mislabelled**: the term is defensible but a caveat is missing, needless, or has the wrong direction.

Units: the model counts damage and HP in tens (HP 110 is `hp := 11`; 50 damage is `damage := 5`).

| Stratum | In pool | Sampled |
|---|---|---|
| Pokémon, exact, with effect text | 667 | 6 |
| Pokémon, exact, no effect text | 307 | 1 |
| Pokémon, with caveats | 391 | 5 |
| Trainer, exact | 64 | 4 |
| Trainer, with caveats | 45 | 3 |
| Special Energy | 9 | 1 |

With no error found in 20 cards, the 95% upper bound on the error rate of the sampled strata is about 14% (1 − 0.05^(1/20)); the sample is stratified, not proportional, so this is indicative only.

---

## 1. Electivire (sv7-47)

Stratum: Pokémon, exact, with effect text. Status: **imported exactly**. Term: `PokemonCards/Standard/Part03.lean:208`.

### Printed

- **Kind:** Pokémon, Stage 1
- **HP:** 150. **Type:** Lightning. **Evolves from:** Electabuzz.
- **Weakness:** Fighting ×2. **Resistance:** none. **Retreat Cost:** 3.
- **Attack: Electroslug** [Lightning] 40. 
- **Attack: Unleash Lightning** [Lightning, Lightning] 220. During your next turn, your Pokémon can't attack. (This includes new Pokémon that come into play.)

### Lean

```lean
/-- Electivire (sv7-47). Records: sv7-47. -/
def sv7_47 : Card := .pokemon
  { name := "Electivire", stage := .stage1, evolvesFrom := some "Electabuzz",
    hp := 15, type := .lightning, retreat := 3, weakness := some .fighting,
    resistance := none, ruleBox := .none, tera := false,
    abilities := [],
    attacks := [
      { name := "Electroslug", cost := [.lightning], damage := 4,
        effect := .skip,
        gx := false },
      { name := "Unleash Lightning", cost := [.lightning, .lightning], damage := 22,
        effect := .linger .own .after (.lock .attack),
        gx := false }] }
```

### Caveats

None (exact).

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 2. Zubat (sv6pt5-27)

Stratum: Pokémon, exact, with effect text. Status: **imported exactly**. Term: `PokemonCards/Standard/Part02.lean:1413`.

### Printed

- **Kind:** Pokémon, Basic
- **HP:** 50. **Type:** Darkness. **Evolves from:** none.
- **Weakness:** Lightning ×2. **Resistance:** Fighting -30. **Retreat Cost:** 1.
- **Attack: Lead** [Darkness] no damage. Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.
- **Attack: Darkness Fang** [Darkness] 10. 

### Lean

```lean
/-- Zubat (sv6pt5-27). Records: sv6pt5-27. -/
def sv6pt5_27 : Card := .pokemon
  { name := "Zubat", stage := .basic, evolvesFrom := none,
    hp := 5, type := .darkness, retreat := 1, weakness := some .lightning,
    resistance := some (.fighting, 3), ruleBox := .none, tera := false,
    abilities := [],
    attacks := [
      { name := "Lead", cost := [.darkness], damage := 0,
        effect := .seq (.move .own .deck .hand (.kind .supporter) (.upTo 1)) .shuffle,
        gx := false },
      { name := "Darkness Fang", cost := [.darkness], damage := 1,
        effect := .skip,
        gx := false }] }
```

### Caveats

None (exact).

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 3. Solrock (me1-75)

Stratum: Pokémon, exact, with effect text. Status: **imported exactly**. Term: `PokemonCards/Standard/Part07.lean:995`.

### Printed

- **Kind:** Pokémon, Basic
- **HP:** 110. **Type:** Fighting. **Evolves from:** none.
- **Weakness:** Grass ×2. **Resistance:** none. **Retreat Cost:** 1.
- **Attack: Cosmic Beam** [Fighting] 70. If you don't have Lunatone on your Bench, this attack does nothing. This attack's damage isn't affected by Weakness or Resistance.

### Lean

```lean
/-- Solrock (me1-75). Records: me1-75, me2pt5-106. -/
def me1_75 : Card := .pokemon
  { name := "Solrock", stage := .basic, evolvesFrom := none,
    hp := 11, type := .fighting, retreat := 1, weakness := some .grass,
    resistance := none, ruleBox := .none, tera := false,
    abilities := [],
    attacks := [
      { name := "Cosmic Beam", cost := [.fighting], damage := 0,
        effect := .ite (.countGe (.bench .own (.named "Lunatone")) 1) (.damage (.const 7) { weak := true, resist := true }) .skip,
        gx := false }] }
```

### Caveats

None (exact).

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 4. Panpour (zsv10pt5-17)

Stratum: Pokémon, exact, with effect text. Status: **imported exactly**. Term: `PokemonCards/Standard/Part06.lean:1403`.

### Printed

- **Kind:** Pokémon, Basic
- **HP:** 70. **Type:** Water. **Evolves from:** none.
- **Weakness:** Lightning ×2. **Resistance:** none. **Retreat Cost:** 1.
- **Attack: Collect** [Colorless] no damage. Draw a card.
- **Attack: Scratch** [Colorless, Colorless] 30. 

### Lean

```lean
/-- Panpour (zsv10pt5-17). Records: zsv10pt5-17, zsv10pt5-101. -/
def zsv10pt5_17 : Card := .pokemon
  { name := "Panpour", stage := .basic, evolvesFrom := none,
    hp := 7, type := .water, retreat := 1, weakness := some .lightning,
    resistance := none, ruleBox := .none, tera := false,
    abilities := [],
    attacks := [
      { name := "Collect", cost := [.colorless], damage := 0,
        effect := .move .own (.top 1) .hand .any .all,
        gx := false },
      { name := "Scratch", cost := [.colorless, .colorless], damage := 3,
        effect := .skip,
        gx := false }] }
```

### Caveats

None (exact).

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 5. Cascoon (me2pt5-14)

Stratum: Pokémon, exact, with effect text. Status: **imported exactly**. Term: `PokemonCards/Standard/Part08.lean:541`.

### Printed

- **Kind:** Pokémon, Stage 1
- **HP:** 90. **Type:** Grass. **Evolves from:** Wurmple.
- **Weakness:** Fire ×2. **Resistance:** none. **Retreat Cost:** 3.
- **Attack: Trading Places** [Grass] no damage. Switch this Pokémon with 1 of your Benched Pokémon.

### Lean

```lean
/-- Cascoon (me2pt5-14). Records: me2pt5-14. -/
def me2pt5_14 : Card := .pokemon
  { name := "Cascoon", stage := .stage1, evolvesFrom := some "Wurmple",
    hp := 9, type := .grass, retreat := 3, weakness := some .fire,
    resistance := none, ruleBox := .none, tera := false,
    abilities := [],
    attacks := [
      { name := "Trading Places", cost := [.grass], damage := 0,
        effect := .switch .own,
        gx := false }] }
```

### Caveats

None (exact).

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 6. Team Rocket's Weezing (sv10-126)

Stratum: Pokémon, exact, with effect text. Status: **imported exactly**. Term: `PokemonCards/Standard/Part05.lean:1893`.

### Printed

- **Kind:** Pokémon, Stage 1
- **HP:** 130. **Type:** Darkness. **Evolves from:** Team Rocket's Koffing.
- **Weakness:** Fighting ×2. **Resistance:** none. **Retreat Cost:** 2.
- **Attack: Explode Together Now** [Darkness, Colorless] 40×. This attack does 40 damage for each Pokémon in play that has "Koffing" or "Weezing" in its name (both yours and your opponent's).

### Lean

```lean
/-- Team Rocket's Weezing (sv10-126). Records: sv10-126, sv10-199. -/
def sv10_126 : Card := .pokemon
  { name := "Team Rocket's Weezing", stage := .stage1, evolvesFrom := some "Team Rocket's Koffing",
    hp := 13, type := .darkness, retreat := 2, weakness := some .fighting,
    resistance := none, ruleBox := .none, tera := false,
    abilities := [],
    attacks := [
      { name := "Explode Together Now", cost := [.darkness, .colorless], damage := 0,
        effect := .damage (.add (.count (.inPlay .own (.and .pokemon (.or (.nameHas "Koffing") (.nameHas "Weezing")))) 4) (.count (.inPlay .opp (.and .pokemon (.or (.nameHas "Koffing") (.nameHas "Weezing")))) 4)),
        gx := false }] }
```

### Caveats

None (exact).

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 7. Aipom (sv6-137)

Stratum: Pokémon, exact, no effect text. Status: **imported exactly**. Term: `PokemonCards/Standard/Part02.lean:1073`.

### Printed

- **Kind:** Pokémon, Basic
- **HP:** 60. **Type:** Colorless. **Evolves from:** none.
- **Weakness:** Fighting ×2. **Resistance:** none. **Retreat Cost:** 1.
- **Attack: Hang Down** [Colorless] 10. 
- **Attack: Playful Kick** [Colorless, Colorless] 20. 

### Lean

```lean
/-- Aipom (sv6-137). Records: sv6-137. -/
def sv6_137 : Card := .pokemon
  { name := "Aipom", stage := .basic, evolvesFrom := none,
    hp := 6, type := .colorless, retreat := 1, weakness := some .fighting,
    resistance := none, ruleBox := .none, tera := false,
    abilities := [],
    attacks := [
      { name := "Hang Down", cost := [.colorless], damage := 1,
        effect := .skip,
        gx := false },
      { name := "Playful Kick", cost := [.colorless, .colorless], damage := 2,
        effect := .skip,
        gx := false }] }
```

### Caveats

None (exact).

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 8. Bronzong (sv8pt5-67)

Stratum: Pokémon, with caveats. Status: **imported with caveats**. Term: `PokemonCards/Standard/Part04.lean:804`.

### Printed

- **Kind:** Pokémon, Stage 1
- **HP:** 130. **Type:** Metal. **Evolves from:** Bronzor.
- **Weakness:** Fire ×2. **Resistance:** Grass -30. **Retreat Cost:** 3.
- **Ability: Protective Bell.** All of your Pokémon take 10 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance).
- **Attack: Heavy Impact** [Metal, Colorless] 50. 

### Lean

```lean
/-- Bronzong (sv8pt5-67). Records: sv8pt5-67. Caveats: staticBench. -/
def sv8pt5_67 : Card := .pokemon
  { name := "Bronzong", stage := .stage1, evolvesFrom := some "Bronzor",
    hp := 13, type := .metal, retreat := 3, weakness := some .fire,
    resistance := some (.grass, 3), ruleBox := .none, tera := false,
    abilities := [
      { name := "Protective Bell", use := .static [{ sel := .own, filt := .any, tgt := none, src := none, need := none, eff := .reduce 1 .any }],
        spot := none, cond := none,
        effect := .fx .skip }],
    attacks := [
      { name := "Heavy Impact", cost := [.metal, .colorless], damage := 5,
        effect := .skip,
        gx := false }] }
```

### Caveats

- `staticBench` (both): a static damage reduction ('takes N less damage from attacks') is subtracted at step 5 of the damage calculation, which only damage to the Active Pokémon passes through: attack damage to a Benched Pokémon takes no reduction in the model (Known gaps, milestone M3: Bench damage takes no bonus, reduction or prevention; milestone M6)

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 9. Solgaleo (me55-105)

Stratum: Pokémon, with caveats. Status: **imported with caveats**. Term: `PokemonCards/Standard/Part10.lean:664`.

### Printed

- **Kind:** Pokémon, Stage 2
- **HP:** 170. **Type:** Metal. **Evolves from:** Cosmoem.
- **Weakness:** Fire ×2. **Resistance:** Grass -30. **Retreat Cost:** 2.
- **Ability: Sunrise.** Once during your turn, if this Pokémon is on your Bench, you may use this Ability. Search your deck for up to 2 Basic Metal Energy cards and attach them to this Pokémon. Then, shuffle your deck.
- **Attack: Sunsteel Strike** [Metal, Metal, Colorless, Colorless] 220. Discard all Energy from this Pokémon.

### Lean

```lean
/-- Solgaleo (me55-105). Records: me55-105. Caveats: selfBench, upTo0. -/
def me55_105 : Card := .pokemon
  { name := "Solgaleo", stage := .stage2, evolvesFrom := some "Cosmoem",
    hp := 17, type := .metal, retreat := 2, weakness := some .fire,
    resistance := some (.grass, 3), ruleBox := .none, tera := false,
    abilities := [
      { name := "Sunrise", use := .once,
        spot := some .bench, cond := none,
        effect := .seq (.fx (.ite (.countGe (.pile .own .deck .any) 1) .skip (.move .own (.top 0) .hand .any (.exactly 1)))) (.seq (.seq (.self (.attach .deck (.energyOf .metal))) (.self (.attach .deck (.energyOf .metal)))) (.fx .shuffle)) }],
    attacks := [
      { name := "Sunsteel Strike", cost := [.metal, .metal, .colorless, .colorless], damage := 22,
        effect := .discardEnergy .own .active .energy .all,
        gx := false }] }
```

### Caveats

- `selfBench` (allows more): 'this Pokémon' on the Bench is a Benched Pokémon chosen when each step resolves (each `SelfOp` step chooses its own, so two attach steps may go to two different Benched Pokémon), and for an on-play Ability the Active Pokémon or a Benched one (Known gaps, Abilities, M8a: `SelfOp`)
- `upTo0` (allows more): 'up to N' in a Trainer or an Ability allows 0 in the model; the rulebook asks for at least 1 outside attacks (2026 rulebook p. 21; Known gaps, zone moves item)

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 10. Pikachu ex (sv8pt5-28)

Stratum: Pokémon, with caveats. Status: **imported with caveats**. Term: `PokemonCards/Standard/Part04.lean:618`.

### Printed

- **Kind:** Pokémon, Basic, Tera, ex
- **HP:** 190. **Type:** Lightning. **Evolves from:** none.
- **Weakness:** Fighting ×2. **Resistance:** none. **Retreat Cost:** 1.
- **Attack: Tail Whap** [Colorless] 30. 
- **Attack: Thunder** [Lightning, Lightning, Colorless] 220. This Pokémon also does 30 damage to itself.
- **Rule text:** As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's).
- **Rule text:** Pokémon ex rule: When your Pokémon ex is Knocked Out, your opponent takes 2 Prize cards.

### Lean

```lean
/-- Pikachu ex (sv8pt5-28). Records: sv8pt5-28. Caveats: recoil. -/
def sv8pt5_28 : Card := .pokemon
  { name := "Pikachu ex", stage := .basic, evolvesFrom := none,
    hp := 19, type := .lightning, retreat := 1, weakness := some .fighting,
    resistance := none, ruleBox := .ex, tera := true,
    abilities := [],
    attacks := [
      { name := "Tail Whap", cost := [.colorless], damage := 3,
        effect := .skip,
        gx := false },
      { name := "Thunder", cost := [.lightning, .lightning, .colorless], damage := 22,
        effect := .selfDamage 3,
        gx := false }] }
```

### Caveats

- `recoil` (both): self-damage ('also does N damage to itself') is written as damage counters (selfDamage): no Weakness, Resistance or modifier applies to it (Known gaps)

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 11. Espurr (sv8-84)

Stratum: Pokémon, with caveats. Status: **imported with caveats**. Term: `PokemonCards/Standard/Part03.lean:1657`.

### Printed

- **Kind:** Pokémon, Basic
- **HP:** 60. **Type:** Psychic. **Evolves from:** none.
- **Weakness:** Darkness ×2. **Resistance:** Fighting -30. **Retreat Cost:** 1.
- **Attack: See Through** [Colorless] no damage. Your opponent reveals their hand.
- **Attack: Psyshot** [Psychic, Colorless] 20. 

### Lean

```lean
/-- Espurr (sv8-84). Records: sv8-84. Caveats: hiddenInfo. -/
def sv8_84 : Card := .pokemon
  { name := "Espurr", stage := .basic, evolvesFrom := none,
    hp := 6, type := .psychic, retreat := 1, weakness := some .darkness,
    resistance := some (.fighting, 3), ruleBox := .none, tera := false,
    abilities := [],
    attacks := [
      { name := "See Through", cost := [.colorless], damage := 0,
        effect := .skip,
        gx := false },
      { name := "Psyshot", cost := [.psychic, .colorless], damage := 2,
        effect := .skip,
        gx := false }] }
```

### Caveats

- `hiddenInfo` (allows more): a sentence that only reveals or looks at cards is a no-op (hidden information is not modelled, Known gaps)

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 12. Cacturne (me6-5)

Stratum: Pokémon, with caveats. Status: **imported with caveats**. Term: `PokemonCards/Standard/Part10.lean:884`.

### Printed

- **Kind:** Pokémon, Stage 1
- **HP:** 130. **Type:** Grass. **Evolves from:** Cacnea.
- **Weakness:** Fire ×2. **Resistance:** none. **Retreat Cost:** 2.
- **Attack: Linear Attack** [Colorless] no damage. This attack does 30 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)
- **Attack: Punishing Needles** [Grass] 10+. This attack does 50 more damage for each of your opponent's Pokémon in play that has an Ability.

### Lean

```lean
/-- Cacturne (me6-5). Records: me6-5. Caveats: abilityByTool, benchMods. -/
def me6_5 : Card := .pokemon
  { name := "Cacturne", stage := .stage1, evolvesFrom := some "Cacnea",
    hp := 13, type := .grass, retreat := 2, weakness := some .fire,
    resistance := none, ruleBox := .none, tera := false,
    abilities := [],
    attacks := [
      { name := "Linear Attack", cost := [.colorless], damage := 0,
        effect := .ite (.countGe (.bench .opp .pokemon) 1) (.choice (.damage (.const 3)) (.benchDamage .opp 3)) (.damage (.const 3)),
        gx := false },
      { name := "Punishing Needles", cost := [.grass], damage := 0,
        effect := .damage (.add (.const 1) (.count (.inPlay .opp (.and .pokemon .hasAbility)) 5)),
        gx := false }] }
```

### Caveats

- `abilityByTool` (both): 'Pokémon that have an Ability' is `Filter.hasAbility`, which reads the printed Abilities and ignores an Ability a Tool gives in the model (Known gaps, filters: whether print counts a Tool's effect as the Pokémon's Ability is not settled); if it does, a Pokémon whose Ability comes from a Tool is not counted where print counts it, and an attacker with such an Ability is not prevented where print prevents its damage
- `benchMods` (both): attack damage to Benched Pokémon takes no bonus, reduction or prevention in the model (Known gaps, milestone M3)

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 13. Energy Search (me3-72)

Stratum: Trainer, exact. Status: **imported exactly**. Term: `PokemonCards/Standard/Part09.lean:305`.

### Printed

- **Kind:** Trainer, Item
- **Rule text:** Search your deck for a Basic Energy card, reveal it, and put it into your hand. Then, shuffle your deck.
- **Rule text:** You may play any number of Item cards during your turn.

### Lean

```lean
/-- Energy Search (me3-72). Records: me3-72. -/
def me3_72 : Card := .trainer "Energy Search" .item
    (.seq (.ite (.countGe (.pile .own .deck .any) 1) .skip (.move .own (.top 0) .hand .any (.exactly 1))) (.seq (.move .own .deck .hand .basicEnergy (.upTo 1)) .shuffle))
```

### Caveats

None (exact).

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 14. Surfer (sv8-187)

Stratum: Trainer, exact. Status: **imported exactly**. Term: `PokemonCards/Standard/Part04.lean:493`.

### Printed

- **Kind:** Trainer, Supporter
- **Rule text:** Switch your Active Pokémon with 1 of your Benched Pokémon. If you do, draw cards until you have 5 cards in your hand.
- **Rule text:** You may play only 1 Supporter card during your turn.

### Lean

```lean
/-- Surfer (sv8-187). Records: sv8-187, sv8-235, me2pt5-200, me2pt5-293. -/
def sv8_187 : Card := .trainer "Surfer" .supporter
    (.seq (.ite (.countGe (.bench .own .pokemon) 1) .skip (.move .own (.top 0) .hand .any (.exactly 1))) (.seq (.switch .own) (.drawTo .own 5)))
```

### Caveats

None (exact).

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 15. Night Stretcher (sv6pt5-61)

Stratum: Trainer, exact. Status: **imported exactly**. Term: `PokemonCards/Standard/Part02.lean:1623`.

### Printed

- **Kind:** Trainer, Item
- **Rule text:** Put a Pokémon or a Basic Energy card from your discard pile into your hand.
- **Rule text:** You may play any number of Item cards during your turn.

### Lean

```lean
/-- Night Stretcher (sv6pt5-61). Records: sv6pt5-61, sv8-251, me1-173, me2pt5-196. -/
def sv6pt5_61 : Card := .trainer "Night Stretcher" .item
    (.move .own .discard .hand (.or .pokemon .basicEnergy) (.exactly 1))
```

### Caveats

None (exact).

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 16. Team Rocket's Petrel (sv10-176)

Stratum: Trainer, exact. Status: **imported exactly**. Term: `PokemonCards/Standard/Part06.lean:377`.

### Printed

- **Kind:** Trainer, Supporter
- **Rule text:** Search your deck for a Trainer card, reveal it, and put it into your hand. Then, shuffle your deck.
- **Rule text:** You may play only 1 Supporter card during your turn.

### Lean

```lean
/-- Team Rocket's Petrel (sv10-176). Records: sv10-176, sv10-226, me2pt5-207. -/
def sv10_176 : Card := .trainer "Team Rocket's Petrel" .supporter
    (.seq (.ite (.countGe (.pile .own .deck .any) 1) .skip (.move .own (.top 0) .hand .any (.exactly 1))) (.seq (.move .own .deck .hand .trainer (.upTo 1)) .shuffle))
```

### Caveats

None (exact).

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 17. Amulet of Hope (sv8-162)

Stratum: Trainer, with caveats. Status: **imported with caveats**. Term: `PokemonCards/Standard/Part04.lean:442`.

### Printed

- **Kind:** Trainer, Pokémon Tool, ACE SPEC
- **Rule text:** If the Pokémon this card is attached to is Knocked Out by damage from an attack from your opponent's Pokémon, search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.
- **Rule text:** You may attach any number of Pokémon Tools to your Pokémon during your turn. You may attach only 1 Pokémon Tool to each Pokémon, and it stays attached.
- **Rule text:** Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached.
- **Rule text:** ACE SPEC: You can't have more than 1 ACE SPEC card in your deck.

### Lean

```lean
/-- Amulet of Hope (sv8-162). Records: sv8-162. Caveats: aceSpec, searchAny, trigKO, upTo0. -/
def sv8_162 : Card := .tool "Amulet of Hope"
  { holder := .pokemon,
    attacks := [],
    abilities := [
      { name := "Amulet of Hope", use := .triggered .koByAttack false,
        spot := none, cond := none,
        effect := .fx (.seq (.move .own .deck .hand .any (.upTo 3)) .shuffle) }] }
```

### Caveats

- `aceSpec` (allows more): the ACE SPEC deck-building limit is not modelled (no deck construction in the model)
- `searchAny` (allows more): a deck search for 'a card' (any card) may find nothing in the model, where print must take at least 1 (2026 rulebook p. 21: 'for any effect that allows you to search your deck or discard pile for any card you want and doesn't specify what kind, you must choose at least 1'; Known gaps, zone moves item: 'a superset elsewhere and for an attack that searches for any card')
- `trigKO` (allows more): 'is Knocked Out by damage from an attack' is read as 'Knocked Out by a Knock Out check while the turn's attack has been made': Knock Outs by damage counters the attack placed, by later rounds of the check, and in the check after a failed Confused attempt also fire it (Known gaps, triggered Abilities, M8b)
- `upTo0` (allows more): 'up to N' in a Trainer or an Ability allows 0 in the model; the rulebook asks for at least 1 outside attacks (2026 rulebook p. 21; Known gaps, zone moves item)

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 18. Potion (me3-83)

Stratum: Trainer, with caveats. Status: **imported with caveats**. Term: `PokemonCards/Standard/Part09.lean:329`.

### Printed

- **Kind:** Trainer, Item
- **Rule text:** Heal 30 damage from 1 of your Pokémon.
- **Rule text:** You may play any number of Item cards during your turn.

### Lean

```lean
/-- Potion (me3-83). Records: me3-83. Caveats: noopPlay. -/
def me3_83 : Card := .trainer "Potion" .item
    (.seq (.ite (.atLeast .own 1) .skip (.ite (.countGe (.bench .own .pokemon) 1) .skip (.move .own (.top 0) .hand .any (.exactly 1)))) (.ite (.countGe (.bench .own .pokemon) 1) (.choice (.heal 3) (.benchHeal 3)) (.heal 3)))
```

### Caveats

- `noopPlay` (allows more): a Trainer (an Item, a Supporter, a Stadium's use) whose effect may do nothing in the model in a state where it could do something (heal 30 damage from 1 of your Pokémon: the model may heal an undamaged one, as it has no test of a Benched Pokémon's damage) can be played to no effect there. The importer reads the usual ruling, not in the rulebook (2026 p. 12 says only 'When you play any Trainer card, do what it says'): a card may not be played when its effect cannot do anything, except that a search of a hidden zone may find nothing; where public information decides it the term states the precondition instead (noop.py; Known gaps, item on plays to no effect)

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 19. Treasure Tracker (sv8pt5-131)

Stratum: Trainer, with caveats. Status: **imported with caveats**. Term: `PokemonCards/Standard/Part04.lean:967`.

### Printed

- **Kind:** Trainer, Item, ACE SPEC
- **Rule text:** You can't have more than 1 ACE SPEC card in your deck.
- **Rule text:** Search your deck for up to 5 Pokémon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck.
- **Rule text:** You may play any number of Item cards during your turn.

### Lean

```lean
/-- Treasure Tracker (sv8pt5-131). Records: sv8pt5-131. Caveats: aceSpec, upTo0. -/
def sv8pt5_131 : Card := .trainer "Treasure Tracker" .item
    (.seq (.ite (.countGe (.pile .own .deck .any) 1) .skip (.move .own (.top 0) .hand .any (.exactly 1))) (.seq (.move .own .deck .hand .tool (.upTo 5)) .shuffle))
```

### Caveats

- `aceSpec` (allows more): the ACE SPEC deck-building limit is not modelled (no deck construction in the model)
- `upTo0` (allows more): 'up to N' in a Trainer or an Ability allows 0 in the model; the rulebook asks for at least 1 outside attacks (2026 rulebook p. 21; Known gaps, zone moves item)

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:


---

## 20. Luminous Energy (sv6-226)

Stratum: Special Energy. Status: **imported exactly**. Term: `PokemonCards/Standard/Part02.lean:1178`.

### Printed

- **Kind:** Energy, Special
- **Rule text:** As long as this card is attached to a Pokémon, it provides every type of Energy but provides only 1 Energy at a time.  If the Pokémon this card is attached to has any other Special Energy attached, this card provides Colorless Energy instead.

### Lean

```lean
/-- Luminous Energy (sv6-226). Records: sv6-226. -/
def sv6_226 : Card := .energy (.special "Luminous Energy" [[.grass, .fire, .water, .lightning, .psychic, .fighting, .darkness, .metal, .fairy, .dragon, .colorless]] { alt := some (.otherSpecial, [[.colorless]]) })
```

### Caveats

None (exact).

### Verdict

- [x] Right   - [ ] Wrong   - [ ] Mislabelled

Notes:

