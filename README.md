#  Smart City Traffic Pipeline  
### Projet de Synthèse – Big Data & Cloud Computing

## Contexte du projet
Ce projet met en œuvre un **pipeline Big Data End-to-End** dédié à l’analyse du **trafic urbain et de la mobilité intelligente** dans une Smart City.

Dans le rôle d’un **Data Engineer**, l’objectif est de :
- Collecter des données de trafic en temps réel (capteurs IoT simulés)
- Les ingérer via un système de streaming
- Les stocker dans un Data Lake
- Les traiter avec un moteur distribué
- Orchestrer le pipeline
- Visualiser des **KPIs décisionnels** pour une municipalité

---

## Architecture Technique

L’infrastructure est **100 % conteneurisée avec Docker** et repose sur les technologies suivantes :

| Couche        | Technologie      | Rôle                        |
|---------------|-----------------|-----------------------------|
| Génération    | Python           | Simulation de capteurs IoT  |
| Ingestion     | Apache Kafka     | Streaming temps réel        |
| Stockage      | HDFS (Hadoop)    | Data Lake                   |
| Traitement    | Apache Spark     | Calculs distribués          |
| Orchestration | Apache Airflow   | Automatisation du pipeline  |
| Visualisation | Grafana          | Dashboards décisionnels     |

**Screenshot**  
> Architecture globale du pipeline 

![WhatsApp Image 2026-01-12 at 07 44 41](https://github.com/user-attachments/assets/7a42e02b-016f-4f0f-9dc9-f6b5adf44969)


---

## Interfaces de Supervision

| Service       | URL locale           | Rôle                           |
|---------------|--------------------|--------------------------------|
| Apache Airflow| http://localhost:8080 | Gestion des DAGs               |
| HDFS NameNode | http://localhost:9870 | Exploration du Data Lake      |
| Spark Master  | http://localhost:8081 | Monitoring des jobs Spark      |
| Grafana       | http://localhost:3000 | Visualisation des KPIs         |


##  Étapes du Pipeline

### 1️ Génération des données IoT
Un script Python simule un réseau de capteurs de trafic urbain.

**Format JSON généré :**
```json
{
  "sensor_id": "S_102",
  "road_id": "R_45",
  "road_type": "Highway",
  "vehicle_count": 120,
  "average_speed": 42.5,
  "occupancy_rate": 0.78,
  "event_time": "2026-01-10T08:15:00"
}

```
##  Logique Métier

- Variation du trafic selon l’heure (heures de pointe et heures creuses)
- Simulation réaliste de la congestion urbaine afin de refléter des conditions réelles

     **Screenshot**  
   
> Terminal ou code source dans `data-generator/`

---

## 2️ Ingestion Streaming – Apache Kafka

Les événements sont produits en continu dans le topic suivant :

```text
traffic-events
```

##  Rôle de Kafka

Apache Kafka joue un rôle central dans l’ingestion des données de trafic en temps réel.

<img width="1211" height="639" alt="image" src="https://github.com/user-attachments/assets/dab6f597-b410-4569-b3bb-f088a3574187" />


### Fonctions principales
- Gestion d’un **haut débit de données IoT**
- Streaming des événements en temps réel
- **Partitionnement** pour assurer la scalabilité et la tolérance aux pannes

---

## 3️ Stockage – Data Lake (HDFS)

Les données brutes issues de Kafka sont stockées dans la **Raw Zone** du Data Lake HDFS :

```bash
/data/raw/traffic/

```
##  Organisation des Données (HDFS)

Les données brutes sont stockées dans la **Raw Zone** du Data Lake HDFS selon une organisation optimisée.

### Principes d’organisation
- Partitionnement par date
- Structuration optimisée pour le traitement analytique ultérieur

 **Screenshot**  
> Interface HDFS NameNode montrant les fichiers stockés

<img width="1674" height="728" alt="image" src="https://github.com/user-attachments/assets/f9e3052f-ac81-478b-b714-cea9a8396223" />


---

## 4️ Traitement Analytique – Apache Spark

Apache Spark lit les données brutes depuis HDFS et calcule les **KPIs de mobilité urbaine**.

### Indicateurs calculés
- Trafic moyen par zone
- Vitesse moyenne par route
- Taux de congestion
- Identification des zones critiques

###  Sortie des données
- **Format** : Parquet  
- **Destination** :
```bash
/data/analytics/traffic/
```

 **Screenshot**  
> Spark UI ou script Spark illustrant le calcul des KPIs

---

## 5️ Orchestration – Apache Airflow

Un **DAG Airflow** automatise l’ensemble du pipeline Big Data :

```text
Kafka → HDFS → Spark → Validation
```
###  Avantages

- Exécution planifiée des workflows
- Gestion des dépendances entre les tâches
- Surveillance et gestion des échecs du pipeline


---

##  Structure du Projet

```text
smart-city-traffic-pipeline/
│
├── airflow/
│   └── dags/
│       └── traffic_pipeline_dag.py
│
├── data-generator/
│   └── generator.py
│
├── kafka/
│   └── producer_config.py
│
├── spark/
│   └── traffic_kpi_job.py
│
├── docker-compose.yml
└── README.md
```
##  Guide de Démarrage Rapide

### 1️ Lancer l’infrastructure

```bash
docker-compose up -d

```
### 2️ Lancer le générateur de données

```bash
python data-generator/generator.py

```
### 3️ Activer le pipeline
- Accéder à l’interface Airflow : http://localhost:8080  
- Activer le DAG **traffic_pipeline**

### 4️ Visualiser les résultats
- Ouvrir Grafana : http://localhost:3000  
- Suivre l’évolution du trafic en temps réel

<img width="1300" height="642" alt="image" src="https://github.com/user-attachments/assets/18aece14-dc88-44f4-9eae-f30ba657ebd2" />

<img width="1342" height="673" alt="image" src="https://github.com/user-attachments/assets/dd14e2c6-ecb7-4d2a-bef6-7ad50b265302" />

<img width="1359" height="680" alt="image" src="https://github.com/user-attachments/assets/3f792c0e-2124-4b3a-a7ad-43f10dcbce35" />

<img width="1375" height="679" alt="image" src="https://github.com/user-attachments/assets/687cd875-406d-4845-88a2-ab0409ec0570" />

---

##  Résultats Attendus

- Pipeline Big Data entièrement fonctionnel
- Données traitées en quasi temps réel
- Dashboards exploitables pour la prise de décision urbaine
- Architecture scalable et prête pour le Cloud

---

## Auteur / Réalisé par

**Hajar Elfallaki-Idrissi** 
**Salma Fennan** 
Étudiantes en Ingénierie Big Data & Cloud Computing  
Projet académique – ENSET

