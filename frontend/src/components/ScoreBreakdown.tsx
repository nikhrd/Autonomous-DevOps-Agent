import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

interface Props {
  score: any;
}

export default function ScoreBreakdown({
  score
}: Props) {

  if (!score)
    return null;

  const data = [
    {
      name: "Score",
      Base: score.base,
      Bonus: score.speed_bonus,
      Penalty:
        score.efficiency_penalty
    }
  ];

  return (
    <BarChart
      width={500}
      height={250}
      data={data}
    >
      <XAxis dataKey="name" />

      <YAxis />

      <Tooltip />

      <Bar dataKey="Base" />

      <Bar dataKey="Bonus" />

      <Bar dataKey="Penalty" />
    </BarChart>
  );
}