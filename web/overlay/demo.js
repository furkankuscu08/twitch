/* Synthetic public events only. Each step uses the same renderer as the socket. */
window.overlayDemoSteps = [
  [{type: "snapshot", round: {running: true}, plant_url: "https://example.org/plant", mines: [], scores: [{owner: "sam", points: 2}, {owner: "alex", points: 1}, {owner: "mira", points: 1}]}],
  [
    {type: "mine_planted", id: "a", owner: "mira", arms_in_s: 30},
    {type: "mine_planted", id: "b", owner: "alex", arms_in_s: 18},
    {type: "mine_planted", id: "c", owner: "sam", arms_in_s: 12},
    {type: "mine_planted", id: "d", owner: "jules", arms_in_s: 5}
  ],
  [{type: "mine_armed", id: "a"}, {type: "mine_armed", id: "b"}],
  [{type: "spark", id: "a"}],
  [{type: "fizzle", id: "a"}],
  [{type: "spark", id: "a"}],
  [{type: "boom", id: "a", owner: "mira", word: "pineapple", planted_ago_s: 125,
    scores: [{owner: "sam", points: 2}, {owner: "mira", points: 2}, {owner: "alex", points: 1}],
    latency_ms: 370, source: "stt", at: 1730000000,
    receipt: [{text: "honestly", hit: false}, {text: "I", hit: false},
      {text: "could", hit: false}, {text: "go", hit: false}, {text: "for", hit: false},
      {text: "some", hit: false}, {text: "pineapple", hit: true}]}],
  [], // Full banner has smoothly shrunk into the compact card.
  [{type: "false_alarm", id: "a", owner: "mira", scores: [{owner: "sam", points: 2}, {owner: "alex", points: 1}, {owner: "mira", points: 1}]}],
  [{type: "spark", id: "b"}],
  [{type: "boom", id: "b", owner: "alex", word: "volcano", planted_ago_s: 142,
    scores: [{owner: "sam", points: 2}, {owner: "alex", points: 2}, {owner: "mira", points: 1}],
    latency_ms: 410, source: "stt", at: 1730000005,
    receipt: [{text: "we", hit: false}, {text: "could", hit: false},
      {text: "hike", hit: false}, {text: "up", hit: false}, {text: "a", hit: false},
      {text: "volcano", hit: true}]}],
  [], // The second boom also remains as a compact card.
  [{type: "reveal", round_top: [{owner: "alex", booms: 1}], scores: [{owner: "sam", points: 2}, {owner: "alex", points: 2}, {owner: "mira", points: 1}], stats: {booms: 1}, duds: [
    {owner: "sam", word: "telescope"},
    {owner: "jules", word: "avocado"}]}],
  [{type: "snapshot", round: {running: false}, plant_url: "", mines: [], scores: [{owner: "sam", points: 2}, {owner: "alex", points: 2}, {owner: "mira", points: 1}]}],
  [{type: "snapshot", round: {running: true}, plant_url: "https://example.org/plant", mines: [], scores: [{owner: "sam", points: 2}, {owner: "alex", points: 2}, {owner: "mira", points: 1}]}]
];

window.overlayDemoCompactSteps = [7, 11];
window.overlayDemoHolds = {6: 3400, 10: 3400};
