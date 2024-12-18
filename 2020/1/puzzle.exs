IO.puts("AoC 2020 - Day 1: Report Repair")
sum_to_find = 2020

case File.read("input.txt") do
  {:ok, contents} ->
    expenses =
      contents
      |> String.split("\n", trim: true)
      |> Enum.map(&String.to_integer(&1))

    expenses
    |> Enum.find_value(fn expense ->
      num = Enum.find(expenses, &(expense + &1 == sum_to_find))
      if num, do: num * expense
    end)
    |> IO.inspect(label: "Part 1")

    expenses
    |> Enum.flat_map(fn expense ->
      Enum.map(expenses, &{expense, &1})
    end)
    |> Enum.find_value(fn {a, b} ->
      c = Enum.find(expenses, &(a + b + &1 == sum_to_find))
      if c, do: a * b * c
    end)
    |> IO.inspect(label: "Part 2")

  {:error, :enoent} ->
    nil
end
