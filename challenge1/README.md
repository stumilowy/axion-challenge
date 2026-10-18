
Zaczynając od analizy danych wygenerowałem wykresy używając kilka popularnych metod dal datasetów o duzej ilości wymiarów

### PCA
![PCA.png](images/PCA.png)

PCA nie przedstawia losowego szumu - widać, że konkretne kolory występują w pewnych obszarach na wykresie, co oznacza, że na pewno istnieją pewne zależności pomiędzy różnymi typami ubrań. Jednak wykres stanowi jedną, dość rozproszoną chmurę punktów, więc tą metodą nie można wywnioskować niczego więcej.

### t-SNE
![t-SNE.png](images/t-SNE.png)
### UMAP
![UMAP.png](images/UMAP.png)

W przypadku t-SNE i UMAP sytuacja wygląda inaczej, ponieważ metody te wyznaczają już cztery konkretne grupy:

* **Grupa obuwia** (3): Sneaker, Sandal, Ankle boot
* **Grupa toreb** (1): Bag
* **Grupa spodni** (1): Trousers
* **Grupa odzieży górnej** (5): T-shirt/Top, Pullover, Dress, Shirt, Coat

Grupy toreb oraz spodni powinny stanowić najmniejszy problem dla modelu, gdyż najtrudniej pomylić je z innym rodzajem ubrań. Jeśli chodzi o grupę obuwia, pomimo że tworzy ona jedną wyspę na wykresie, widać w jej obrębie konkretne obszary, w których występują poszczególne rodzaje butów.

Inaczej sprawa się ma w przypadku grupy odzieży górnej, w której można by teoretycznie wyznaczyć dwie podgrupy:

1. **Pierwsza (mniej problematyczna):** T-shirt/Top oraz Dress
2. **Druga podgrupa:** Pullover, Shirt, Coat

Elementy tej drugiej podgrupy są silnie wymieszane ze sobą i nie widać tam żadnych konkretnych granic występowania danego typu ubrania.

![type-mean.png](images/type-mean.png)

W uśrednieniu *pullover*, *coat* i *shirt* wyglądają bardzo podobnie, dlatego model będzie miał największy problem z ich poprawnym rozpoznawaniem.

W celu weryfikacji tej hipotezy przetestuje dwa podejścia:

* **Model 1:** Trenowany na bazowym data setcie.
* **Model 2:** Trenowany na zmodyfikowanym zestawie danych, w którym *pullover*, *coat* i *shirt* zostaną scalone w jeden supertyp ubrań.

Jeśli accuracy drugiego modelu okaże się znacząco wyższe, będzie to bezpośrednim potwierdzeniem Twojej hipotezy.


