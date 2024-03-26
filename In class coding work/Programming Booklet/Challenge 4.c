#include <stdio.h>
int main(void) {
  float speed,time,distance;
  float distance_limit,time_limit,speed_limit;
  printf("What was the speed of the car and the time at that speed \n");
  scanf("%f %f",&speed,&time);
  distance=speed*time;
  printf("The distance travelled by the car %f \n",distance);
  printf("What is the distance that you want to travel in a certain amount of time \n");
  scanf("%f %f",&distance_limit,&time_limit);
  speed_limit=distance_limit/time_limit;
  printf("You would have to travel at a speed of %f \n",speed_limit);
  return 0;
}
