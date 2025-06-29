

import java.awt.Point;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.EnumMap;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Random;
import java.util.Set;

public class Pentomino {

    private static final int YSPAN = 6;
    private static final int XSPAN = 10;
    private static final int PENTO = 5;

    public static void main(String[] args) {
        Board board = new Board(YSPAN, XSPAN);
        board.print();

        List<Piece> pieces = new ArrayList<>();
        for (PieceLabel label : PieceLabel.values()) {
            pieces.add(new Piece(label));
        }
        Collections.shuffle(pieces);

        long startTime = System.nanoTime();

        PriorityQueue<int[]> cellQueue = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        cellQueue.add(new int[]{0, 0, 0}); // priority, y, x

        FitStatistics fitStatistics = new FitStatistics(pieces);
        SearchStatistics searchStatistics = new SearchStatistics();
        PieceChoiceStrategy pieceChoiceStrategy = new FitDifficultPieceChoice();

        try {
            Board answer = backtrack(cellQueue, pieces, board, fitStatistics, searchStatistics, pieceChoiceStrategy);
            long endTime = System.nanoTime();

            System.out.println("#fit rate");
            for (Map.Entry<PieceLabel, Double> entry : fitStatistics.listFitRate()) {
                System.out.printf("%s: %.3f%n", entry.getKey(), entry.getValue());
            }

            System.out.println("\n#reach distribution");
            for (Map.Entry<Integer, Double> entry : searchStatistics.reachDistribution()) {
                System.out.printf("%2d: %.4f%n", entry.getKey(), entry.getValue());
            }

            System.out.println();
            double elapsed = (endTime - startTime) / 1e9;
            System.out.printf("elapsed time [s]: %.2f%n", elapsed);
            System.out.println("total search trial: " + searchStatistics.totalTrial());
            System.out.printf("mean fit rate: %.2f%n", fitStatistics.meanFitRate());
            System.out.printf("mean reached depth: %.2f%n", searchStatistics.meanReachedDepth());
            System.out.println();
            answer.print();

        } catch (NoAnswer e) {
            System.out.println("No solution found.");
        }
    }

    private static Board backtrack(
            PriorityQueue<int[]> cellQueue,
            List<Piece> remainingPieces,
            Board board,
            FitStatistics fitStatistics,
            SearchStatistics searchStatistics,
            PieceChoiceStrategy pieceChoiceStrategy
    ) throws NoAnswer {
        while (!cellQueue.isEmpty()) {
            int[] cell = cellQueue.poll();
            int y = cell[1];
            int x = cell[2];

            if (!board.isEmptyAt(y, x)) {
                continue;
            }

            List<Piece> piecesNotTried = new ArrayList<>(remainingPieces);

            while (!piecesNotTried.isEmpty()) {
                Piece piece = pieceChoiceStrategy.pop(piecesNotTried, fitStatistics);
                fitStatistics.countupTrial(piece.getLabel());

                for (MinoPosition piecePosition : piece.possiblePositions(y, x, board)) {
                    fitStatistics.countupFit(piece.getLabel());

                    Board board2 = board.deepCopy();
                    board2.put(piecePosition, piece.getLabel());

                    List<Piece> remainingPieces2 = new ArrayList<>(remainingPieces);
                    remainingPieces2.remove(piece);

                    PriorityQueue<int[]> cellQueue2 = new PriorityQueue<>(cellQueue);
                    int[][] four = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

                    Set<Point> neighbors = new HashSet<>();
                    for (Point p : piecePosition.getMinos()) {
                        for (int[] dir : four) {
                            Point neighbor = new Point(p.x + dir[1], p.y + dir[0]);
                            if (board2.isEmptyAt(neighbor.y, neighbor.x)) {
                                neighbors.add(neighbor);
                            }
                        }
                    }

                    for (Point neighbor : neighbors) {
                        int openEdges = 0;
                        for (int[] dir : four) {
                            if (board2.isEmptyAt(neighbor.y + dir[0], neighbor.x + dir[1])) {
                                openEdges++;
                            }
                        }
                        cellQueue2.add(new int[]{prioritize(openEdges, neighbor.y, neighbor.x, board2.getNy(), board2.getNx()), neighbor.y, neighbor.x});
                    }

                    try {
                        return backtrack(cellQueue2, remainingPieces2, board2, fitStatistics, searchStatistics, pieceChoiceStrategy);
                    } catch (NoAnswer e) {
                        // continue
                    }
                }
            }

            searchStatistics.countup(board.putHistory.size());
            if (searchStatistics.totalTrial() % 1000 == 0) {
                System.out.println("#search trial: " + searchStatistics.totalTrial() + ": " + board.putHistory);
                board.print();
                System.out.println();
            }

            throw new NoAnswer();
        }

        return board;
    }

    private static int prioritize(int openEdges, int y, int x, int yspan, int xspan) {
        return openEdges;
    }

    static class NoAnswer extends Exception {
    }
}

enum PieceLabel {
    O, P, Q, R, S, T, U, V, W, X, Y, Z
}

class PieceShape {
    public static final Map<PieceLabel, int[][]> shapes = new EnumMap<>(PieceLabel.class);

    static {
        shapes.put(PieceLabel.O, new int[][]{{'@', '@', '@', '@', '@'}});
        shapes.put(PieceLabel.P, new int[][]{{'@', '@', '@'}, {'@', '@', 0}});
        shapes.put(PieceLabel.Q, new int[][]{{'@', '@', '@', '@'}, {'@', 0, 0, 0}});
        shapes.put(PieceLabel.R, new int[][]{{'@', '@', 0}, {0, '@', '@'}, {0, '@', 0}});
        shapes.put(PieceLabel.S, new int[][]{{0, '@', '@', '@'}, {'@', '@', 0, 0}});
        shapes.put(PieceLabel.T, new int[][]{{'@', 0, 0}, {'@', '@', '@'}, {'@', 0, 0}});
        shapes.put(PieceLabel.U, new int[][]{{'@', '@', '@'}, {'@', 0, '@'}});
        shapes.put(PieceLabel.V, new int[][]{{'@', '@', '@'}, {'@', 0, 0}, {'@', 0, 0}});
        shapes.put(PieceLabel.W, new int[][]{{0, '@', '@'}, {'@', '@', 0}, {'@', 0, 0}});
        shapes.put(PieceLabel.X, new int[][]{{0, '@', 0}, {'@', '@', '@'}, {0, '@', 0}});
        shapes.put(PieceLabel.Y, new int[][]{{'@', '@', '@', '@'}, {0, '@', 0, 0}});
        shapes.put(PieceLabel.Z, new int[][]{{'@', '@', 0}, {0, '@', 0}, {0, '@', '@'}});
    }
}

class MinoPosition {
    private List<Point> minos;

    public MinoPosition(List<Point> minos) {
        this.minos = new ArrayList<>(minos);
    }

    public void turnFlip(int factor) {
        List<Point> newPosition = new ArrayList<>();
        for (Point p : minos) {
            int y = p.y;
            int x = p.x;
            int ny, nx;
            switch (factor) {
                case 0: ny = y; nx = x; break;
                case 1: ny = x; nx = -y; break;
                case 2: ny = -y; nx = -x; break;
                case 3: ny = -x; nx = y; break;
                case 4: ny = y; nx = -x; break;
                case 5: ny = -x; nx = -y; break;
                case 6: ny = -y; nx = x; break;
                case 7: ny = x; nx = y; break;
                default: throw new IllegalArgumentException("Invalid factor");
            }
            newPosition.add(new Point(nx, ny));
        }
        newPosition.sort(Comparator.comparingInt((Point p) -> p.y).thenComparingInt(p -> p.x));
        this.minos = newPosition;
    }

    public void move(int baseCell, int y, int x) {
        Point p0 = minos.get(baseCell);
        List<Point> newMinos = new ArrayList<>();
        for (Point p : minos) {
            newMinos.add(new Point(p.x - p0.x + x, p.y - p0.y + y));
        }
        this.minos = newMinos;
    }

    public List<Point> getMinos() {
        return minos;
    }

    @Override
    public String toString() {
        return "MinoPosition(" + minos + ")";
    }
}

class Board {
    PieceLabel[][] cells;
    final List<PieceLabel> putHistory = new ArrayList<>();

    public Board(int ny, int nx) {
        cells = new PieceLabel[ny][nx];
    }

    public int getNy() {
        return cells.length;
    }

    public int getNx() {
        return cells[0].length;
    }

    public boolean isEmptyAt(int y, int x) {
        return y >= 0 && y < getNy() && x >= 0 && x < getNx() && cells[y][x] == null;
    }

    public boolean canAccept(MinoPosition minos) {
        for (Point p : minos.getMinos()) {
            if (!isEmptyAt(p.y, p.x)) {
                return false;
            }
        }
        return true;
    }

    public void put(MinoPosition position, PieceLabel k) {
        for (Point p : position.getMinos()) {
            cells[p.y][p.x] = k;
        }
        putHistory.add(k);
    }

    public void print() {
        for (PieceLabel[] row : cells) {
            StringBuilder sb = new StringBuilder();
            for (PieceLabel c : row) {
                sb.append(c == null ? "." : c.name()).append(" ");
            }
            System.out.println(colorString(sb.toString()));
        }
    }

    private static String colorString(String plainString) {
        final String RESET = "\033[0m";
        final Map<PieceLabel, String> colorMap = new EnumMap<>(PieceLabel.class);
        colorMap.put(PieceLabel.O, "\033[31m"); // RED
        colorMap.put(PieceLabel.P, "\033[32m"); // GREEN
        colorMap.put(PieceLabel.Q, "\033[33m"); // YELLOW
        colorMap.put(PieceLabel.R, "\033[34m"); // BLUE
        colorMap.put(PieceLabel.S, "\033[35m"); // MAGENTA
        colorMap.put(PieceLabel.T, "\033[36m"); // CYAN
        colorMap.put(PieceLabel.U, "\033[91m"); // LIGHT_RED
        colorMap.put(PieceLabel.V, "\033[92m"); // LIGHT_GREEN
        colorMap.put(PieceLabel.W, "\033[93m"); // LIGHT_YELLOW
        colorMap.put(PieceLabel.X, "\033[94m"); // LIGHT_BLUE
        colorMap.put(PieceLabel.Y, "\033[95m"); // LIGHT_MAGENTA
        colorMap.put(PieceLabel.Z, "\033[96m"); // LIGHT_CYAN

        StringBuilder coloredString = new StringBuilder();
        for (String s : plainString.split(" ")) {
            try {
                PieceLabel label = PieceLabel.valueOf(s);
                if (colorMap.containsKey(label)) {
                    coloredString.append(colorMap.get(label)).append(s).append(RESET).append(" ");
                } else {
                    coloredString.append(s).append(" ");
                }
            } catch (IllegalArgumentException e) {
                coloredString.append(s).append(" ");
            }
        }
        return coloredString.toString();
    }

    public Board deepCopy() {
        Board newBoard = new Board(getNy(), getNx());
        for (int i = 0; i < getNy(); i++) {
            for (int j = 0; j < getNx(); j++) {
                newBoard.cells[i][j] = this.cells[i][j];
            }
        }
        newBoard.putHistory.addAll(this.putHistory);
        return newBoard;
    }
}

class Piece {
    private static final int PENTO = 5;
    private final PieceLabel label;
    private final List<Point> minos;

    public Piece(PieceLabel label) {
        this.label = label;
        int[][] shape = PieceShape.shapes.get(label);
        this.minos = new ArrayList<>();
        for (int y = 0; y < shape.length; y++) {
            for (int x = 0; x < shape[y].length; x++) {
                if (shape[y][x] != 0) {
                    this.minos.add(new Point(x, y));
                }
            }
        }
    }

    public PieceLabel getLabel() {
        return label;
    }

    public List<MinoPosition> possiblePositions(int y, int x, Board board) {
        List<MinoPosition> positions = new ArrayList<>();
        List<Integer> turnFactors = new ArrayList<>();
        for (int i = 0; i < 8; i++) {
            turnFactors.add(i);
        }
        Collections.shuffle(turnFactors);

        List<Integer> cellIndexes = new ArrayList<>();
        for (int i = 0; i < PENTO; i++) {
            cellIndexes.add(i);
        }
        Collections.shuffle(cellIndexes);

        Set<List<Point>> done = new HashSet<>();
        for (int factor : turnFactors) {
            for (int centerCell : cellIndexes) {
                MinoPosition position = new MinoPosition(this.minos);
                position.turnFlip(factor);
                position.move(centerCell, y, x);

                List<Point> key = position.getMinos();
                if (done.contains(key)) {
                    continue;
                }
                done.add(key);

                if (board.canAccept(position)) {
                    positions.add(position);
                }
            }
        }
        return positions;
    }
}

class FitStatistics {
    private final Map<PieceLabel, Integer> trial = new EnumMap<>(PieceLabel.class);
    private final Map<PieceLabel, Integer> fit = new EnumMap<>(PieceLabel.class);

    public FitStatistics(List<Piece> pieces) {
        for (Piece p : pieces) {
            trial.put(p.getLabel(), 1);
            fit.put(p.getLabel(), 1);
        }
    }

    public void countupTrial(PieceLabel piece) {
        trial.put(piece, trial.get(piece) + 1);
    }

    public void countupFit(PieceLabel piece) {
        fit.put(piece, fit.get(piece) + 1);
    }

    public double fitRate(PieceLabel piece) {
        return (double) fit.get(piece) / trial.get(piece);
    }

    public List<Map.Entry<PieceLabel, Double>> listFitRate() {
        List<Map.Entry<PieceLabel, Double>> rateList = new ArrayList<>();
        for (PieceLabel p : trial.keySet()) {
            rateList.add(Map.entry(p, fitRate(p)));
        }
        rateList.sort(Map.Entry.comparingByValue());
        return rateList;
    }

    public double meanFitRate() {
        return (double) fit.values().stream().mapToInt(Integer::intValue).sum() / trial.values().stream().mapToInt(Integer::intValue).sum();
    }
}

class SearchStatistics {
    private final Map<Integer, Integer> reachedDepthCount = new HashMap<>();

    public void countup(int reachedDepth) {
        reachedDepthCount.put(reachedDepth, reachedDepthCount.getOrDefault(reachedDepth, 0) + 1);
    }

    public int totalTrial() {
        return reachedDepthCount.values().stream().mapToInt(Integer::intValue).sum();
    }

    public double meanReachedDepth() {
        return (double) reachedDepthCount.entrySet().stream().mapToLong(e -> (long) e.getKey() * e.getValue()).sum() / totalTrial();
    }

    public List<Map.Entry<Integer, Double>> reachDistribution() {
        List<Map.Entry<Integer, Double>> reachd = new ArrayList<>();
        long total = totalTrial();
        for (Map.Entry<Integer, Integer> entry : reachedDepthCount.entrySet()) {
            reachd.add(Map.entry(entry.getKey(), (double) entry.getValue() / total));
        }
        reachd.sort(Map.Entry.comparingByKey());
        return reachd;
    }
}

interface PieceChoiceStrategy {
    Piece pop(List<Piece> pieces, FitStatistics fitStatistics);
}

class FitDifficultPieceChoice implements PieceChoiceStrategy {
    @Override
    public Piece pop(List<Piece> pieces, FitStatistics fitStatistics) {
        pieces.sort(Comparator.comparingDouble(p -> fitStatistics.fitRate(p.getLabel())));
        return pieces.remove(pieces.size() - 1);
    }
}

class FitEasyPieceChoice implements PieceChoiceStrategy {
    @Override
    public Piece pop(List<Piece> pieces, FitStatistics fitStatistics) {
        pieces.sort(Comparator.comparingDouble((Piece p) -> fitStatistics.fitRate(p.getLabel())).reversed());
        return pieces.remove(pieces.size() - 1);
    }
}

class RandomPieceChoice implements PieceChoiceStrategy {
    @Override
    public Piece pop(List<Piece> pieces, FitStatistics fitStatistics) {
        Collections.shuffle(pieces);
        return pieces.remove(pieces.size() - 1);
    }
}
