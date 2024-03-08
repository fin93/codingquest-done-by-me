import java.util.HashMap;

public class App {
    public static void main(String[] args) throws Exception {
        // System.out.println("Hello, World!");
        new App();
    }

    public int get_min(int[] i) {
        int min = 1000000000;
        for (int j = 0; j < i.length; j++) {
            if (i[j] < min) {
                min = i[j];
            }
        }
        return min;
    }

    public App() {
        Filereader x = new Filereader();
        String[] data = x.getContents();
        String[] name;
        String[] why;
        int cost;
        int[] costs = new int[20];
        
        HashMap<String, inn> relations = new HashMap<String, inn>();
        relations.put("Seat", new inn(1));
        relations.put("Tax", new inn(1));
        relations.put("Fee", new inn(1));
        relations.put("Luggage", new inn(1));
        relations.put("Meals", new inn(1));

        relations.put("Rebate", new inn(-1));
        relations.put("Discount", new inn(-1));




        HashMap<String, inn> airlines = new HashMap<String, inn>();


        for (int i = 0; i < data.length; i++) {
            // System.out.println(data[i].replaceAll("\\s", ""));
            data[i] = data[i].replaceAll("\\s", "");
            name = data[i].split(":");
            why = name[1].split("(?<=\\d)(?=\\D)|(?=\\d)(?<=\\D)");
            cost = Integer.valueOf(why[1]);

            if (airlines.containsKey(name[0])) {
                airlines.get(name[0]).set(relations.get(why[0]).getInn() * cost);
            }
            else {
                airlines.put(name[0], new inn(relations.get(why[0]).getInn() * cost));
            }

            // System.out.println(cost);

            // System.out.println(relations.get(why[0]).getInn());
            
        }
        int which_cost = 0;
        for (String string : airlines.keySet()) {
            System.out.print(string + ": ");
            System.out.println(airlines.get(string).getInn());

            costs[which_cost] = airlines.get(string).getInn();
            which_cost++;
        }
        // System.out.println(costs);
        System.out.println(get_min(costs));
    }
}
