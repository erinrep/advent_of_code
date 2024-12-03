IO.puts("AoC 2020 - Day 3: Toboggan Trajectory")

case File.read("input.txt") do
  {:ok, contents} ->
    rows =
      contents
      |> String.split("\n", trim: true)
      |> Enum.map(&String.split(&1, "", trim: true))

    rows
    |> Enum.with_index()
    |> Enum.map(fn {row, index} ->
      position = index * 3
      extra_cols = Kernel.ceil((position + 1) / Enum.count(row))

      row
      |> List.duplicate(extra_cols)
      |> Enum.concat()
      |> Enum.at(position)
    end)
    |> Enum.count(&(&1 == "#"))
    |> IO.inspect(label: "Part 1")

  {:error, :enoent} ->
    nil
end
