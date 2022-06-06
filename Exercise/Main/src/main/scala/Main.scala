
import java.io.File
import scala.io.StdIn.readLine
import scala.util.Try

//The default path src/main/scala/Files
//=> = Expression evaluated when parameter is accessed.
object Main extends App{

  val currentPath : String = args(0)

  val files = Program.getFiles(currentPath)
  val filenames = new File(currentPath).list

  println(files.length + " files read in the path " + currentPath)
  println()

  val data = Array.ofDim[String](files.length, 1)
  for (i <- files.indices){
    data(i) = Program.extract(files(i).toString)
    Program.printall(data(i))
  }

  Program.iterate(filenames, data)

}

object Program{

  //Calculate score
  def calculateScore(hits : Array[Int], data : Array[Array[String]]) : Array[Double] = {
    val scores = new Array[Double](hits.length)

    //Basically percentage scoring.
    for(i <- hits.indices){
      scores(i) = hits(i).toDouble/data(i).length
    }
    scores
  }

  //Returns txt files in the folder
  def getFiles(dir : String) : Array[File] = {
    new java.io.File(dir).listFiles.filter(_.getName.endsWith(".txt"))
  }

  //Extract words
  def extract(file : String) : Array[String] = {
    //Create empty array
    var c : Array[String] = Array()

    //Filter away whitespaces and items not a-z
    for(s <- scala.io.Source.fromFile(file).getLines.toArray){
      c = c ++ s.toLowerCase.split("[^a-z]| +")
    }

    //Return with distinct values in array
    c.distinct
  }

  //Keeps iterating the search
  def iterate(filenames : Array[String], data : Array[Array[String]]) : Unit = {
    val points = new Array[Int](data.length)
    print("search> ")
    val words = readLine().toLowerCase()

    //If quit, the system exits
    if(words == ":quit"){
      System.exit(0)
    }

    val wordsArr = words.split(" +").distinct

    //Check input to words data (Contains is basically the search)
    for(w <- wordsArr; i <- data.indices){
      if (data(i).contains(w)){
        points(i) += 1
      }
    }

    val scores = calculateScore(points, data)

    //Sorts highest score first.
    val scorebyfile = (scores zip filenames).sortBy(_._1)(Ordering[Double].reverse)

    //Print top 10 scores
    for(i <- 0 to 10){
      if(i < scorebyfile.length){
        println(scorebyfile(i)._2 + ": " + scorebyfile(i)._1 * 100 + " %")
      }
    }

    iterate(filenames, data)
  }

  //Print all values in an array
  def printall(list : Array[_]): Unit ={
    print("[")
    for (i <- list){
      print(s"$i, ")
    }
    print("]\n")

  }

}